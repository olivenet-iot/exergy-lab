import { formatNumber, formatCurrency } from '../../utils/formatters';

const FactoryMetricBar = ({ aggregates, integrationPotential }) => {
  if (!aggregates) return null;

  const efficiency = aggregates.factory_exergy_efficiency_pct;
  const effColor =
    efficiency >= 70
      ? 'text-green-600'
      : efficiency >= 50
        ? 'text-amber-600'
        : 'text-red-600';

  const cards = [
    {
      label: 'TOPLAM GIRIS',
      value: `${formatNumber(aggregates.total_exergy_input_kW, 1)} kW`,
      color: 'text-slate-700',
    },
    {
      label: 'TOPLAM CIKIS',
      value: `${formatNumber(aggregates.total_exergy_output_kW, 1)} kW`,
      color: 'text-green-600',
    },
    {
      label: 'TOPLAM YIKIM',
      value: `${formatNumber(aggregates.total_exergy_destroyed_kW, 1)} kW`,
      color: 'text-red-600',
    },
    {
      label: 'FABRIKA VERIMI',
      value: efficiency != null ? `%${formatNumber(efficiency)}` : '—',
      color: efficiency != null ? effColor : 'text-slate-400',
    },
    {
      label: 'YILLIK KAYIP',
      value: formatCurrency(aggregates.total_annual_loss_EUR),
      color: 'text-red-600',
    },
    {
      label: 'TASARRUF POTANSIYELI',
      value: integrationPotential != null ? formatCurrency(integrationPotential) : '—',
      color: 'text-green-600',
      highlight: true,
    },
  ];

  return (
    <div className="flex items-stretch gap-3 overflow-x-auto">
      {cards.map((card) => (
        <div
          key={card.label}
          className={`flex-1 min-w-[130px] flex flex-col items-center justify-center py-2 px-3 rounded-lg ${
            card.highlight ? 'bg-green-50' : 'bg-slate-50'
          }`}
        >
          <span className="text-xs uppercase tracking-wider text-slate-500 mb-1">
            {card.label}
          </span>
          <span className={`font-mono font-semibold text-lg ${card.color}`}>
            {card.value}
          </span>
        </div>
      ))}
    </div>
  );
};

export default FactoryMetricBar;
