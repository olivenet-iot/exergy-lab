import { Activity, DollarSign, BarChart3 } from 'lucide-react';
import { formatNumber } from '../../utils/formatters';

const EXTRA_METRICS = {
  lmtd_K:          { label: 'LMTD', unit: 'K' },
  effectiveness:   { label: 'Isil Etkinlik', unit: '%', scale: 100 },
  bejan_number:    { label: 'Bejan Sayisi', unit: '' },
  heat_duty_kW:    { label: 'Isi Yuku', unit: 'kW' },
  shaft_power_kW:  { label: 'Saft Gucu', unit: 'kW' },
  electrical_power_kW: { label: 'Elektrik Gucu', unit: 'kW' },
  chp_exergy_efficiency_pct: { label: 'CHP Exergy Verimi', unit: '%' },
  water_removed_kg_h: { label: 'Su Uzaklastirma', unit: 'kg/h' },
  specific_energy_kJ_kg_water: { label: 'Spesifik Enerji', unit: 'kJ/kg-su' },
  thermal_efficiency_pct: { label: 'Termal Verim', unit: '%' },
  combustion_loss_kW: { label: 'Yanma Kaybi', unit: 'kW' },
  flue_gas_loss_kW: { label: 'Baca Gazi Kaybi', unit: 'kW' },
  cop: { label: 'COP', unit: '' },
  cop_carnot: { label: 'Carnot COP', unit: '' },
  kw_per_ton: { label: 'kW/ton', unit: 'kW/ton' },
  hydraulic_power_kW: { label: 'Hidrolik Guc', unit: 'kW' },
  wire_to_water_efficiency_pct: { label: 'Wire-to-Water Verim', unit: '%' },
  throttle_loss_kW: { label: 'Kisma Kaybi', unit: 'kW' },
};

const MetricRow = ({ label, value, unit }) => (
  <div className="flex items-center justify-between py-1.5">
    <span className="text-sm text-gray-600">{label}</span>
    <span className="font-mono font-semibold text-sm text-gray-900">
      {formatNumber(value)} {unit}
    </span>
  </div>
);

const MetricGroup = ({ icon: Icon, title, children, iconColor }) => (
  <div className="bg-white rounded-xl border border-gray-200 p-5">
    <div className="flex items-center gap-2 mb-3">
      <Icon className={`w-4 h-4 ${iconColor}`} />
      <h4 className="text-sm font-semibold text-gray-900">{title}</h4>
    </div>
    <div className="divide-y divide-gray-50">{children}</div>
  </div>
);

const DetailedMetrics = ({ metrics, heatRecovery }) => {
  if (!metrics) return null;

  // Build equipment-specific rows
  const extraRows = Object.entries(EXTRA_METRICS)
    .filter(([key]) => metrics[key] != null)
    .map(([key, meta]) => ({
      label: meta.label,
      value: meta.scale ? metrics[key] * meta.scale : metrics[key],
      unit: meta.unit,
    }));

  // Check for exergoeconomic data
  const hasExergoeconomic = metrics.exergoeconomic_f_factor != null;

  return (
    <div className="space-y-4">
      {/* Exergy Balance */}
      <MetricGroup icon={Activity} title="Ekserji Dengesi" iconColor="text-blue-500">
        <MetricRow label="Exergy Girisi" value={metrics.exergy_input_kW} unit="kW" />
        <MetricRow label="Faydali Exergy" value={metrics.exergy_output_kW} unit="kW" />
        <MetricRow label="Exergy Yikimi" value={metrics.exergy_destroyed_kW} unit="kW" />
        {metrics.exergy_destroyed_avoidable_kW != null && (
          <>
            <MetricRow label="Onlenebilir Yikim" value={metrics.exergy_destroyed_avoidable_kW} unit="kW" />
            <MetricRow label="Onlenemez Yikim" value={metrics.exergy_destroyed_unavoidable_kW} unit="kW" />
            <MetricRow label="Onlenebilir Oran" value={metrics.avoidable_ratio_pct} unit="%" />
          </>
        )}
        {extraRows.map((row) => (
          <MetricRow key={row.label} label={row.label} value={row.value} unit={row.unit} />
        ))}
      </MetricGroup>

      {/* Economic Indicators */}
      {hasExergoeconomic && (
        <MetricGroup icon={DollarSign} title="Ekonomik Gostergeler" iconColor="text-amber-500">
          <MetricRow label="f Faktoru" value={metrics.exergoeconomic_f_factor} unit="" />
          <MetricRow label="r Faktoru" value={metrics.exergoeconomic_r_factor} unit="" />
          <MetricRow label="Z (EUR/h)" value={metrics.exergoeconomic_Z_dot_eur_h} unit="EUR/h" />
          <MetricRow label="C_D (EUR/h)" value={metrics.exergoeconomic_C_dot_destruction_eur_h} unit="EUR/h" />
          {metrics.exergoeconomic_c_product_eur_kWh != null && (
            <MetricRow label="c_P (EUR/kWh)" value={metrics.exergoeconomic_c_product_eur_kWh} unit="EUR/kWh" />
          )}
          {metrics.exergoeconomic_total_cost_rate_eur_h != null && (
            <MetricRow label="Z+C_D (EUR/h)" value={metrics.exergoeconomic_total_cost_rate_eur_h} unit="EUR/h" />
          )}
        </MetricGroup>
      )}

      {/* Annual Impact */}
      <MetricGroup icon={BarChart3} title="Yillik Etki" iconColor="text-emerald-500">
        {metrics.annual_loss_kWh != null && (
          <MetricRow label="Yillik Kayip" value={metrics.annual_loss_kWh} unit="kWh" />
        )}
        {metrics.annual_cost_eur != null && (
          <MetricRow label="Yillik Maliyet" value={metrics.annual_cost_eur} unit="EUR" />
        )}
        {heatRecovery?.potential_kW != null && (
          <MetricRow label="Isi Geri Kazanim" value={heatRecovery.potential_kW} unit="kW" />
        )}
        {heatRecovery?.annual_savings_eur != null && (
          <MetricRow label="Potansiyel Tasarruf" value={heatRecovery.annual_savings_eur} unit="EUR/yil" />
        )}
      </MetricGroup>
    </div>
  );
};

export default DetailedMetrics;
