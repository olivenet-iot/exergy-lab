import { formatNumber, formatCurrency } from '../../utils/formatters';

const ESI_GRADE_COLORS = {
  A: 'text-emerald-400',
  B: 'text-green-400',
  C: 'text-lime-400',
  D: 'text-amber-400',
  E: 'text-orange-400',
  F: 'text-red-400',
};

const FactoryMetricBar = ({ aggregates, integrationPotential, gapAnalysis }) => {
  if (!aggregates) return null;

  const efficiency = aggregates.factory_exergy_efficiency_pct;
  const effColor =
    efficiency >= 70
      ? 'text-emerald-400'
      : efficiency >= 50
        ? 'text-amber-400'
        : 'text-red-400';

  const cards = [
    {
      label: 'TOPLAM GİRİŞ',
      value: `${formatNumber(aggregates.total_exergy_input_kW, 1)} kW`,
      color: 'text-white',
    },
    {
      label: 'TOPLAM ÇIKIŞ',
      value: `${formatNumber(aggregates.total_exergy_output_kW, 1)} kW`,
      color: 'text-emerald-400',
    },
    {
      label: 'TOPLAM YIKIM',
      value: `${formatNumber(aggregates.total_exergy_destroyed_kW, 1)} kW`,
      color: 'text-red-400',
    },
    {
      label: 'FABRİKA VERİMİ',
      value: efficiency != null ? `%${formatNumber(efficiency)}` : '—',
      color: efficiency != null ? effColor : 'text-slate-400',
    },
    {
      label: 'YILLIK KAYIP',
      value: formatCurrency(aggregates.total_annual_loss_EUR),
      color: 'text-red-400',
    },
    {
      label: 'TASARRUF POTANSİYELİ',
      value: integrationPotential != null ? formatCurrency(integrationPotential) : '—',
      color: 'text-emerald-400',
      highlight: true,
    },
  ];

  // Add ESI grade and BAT gap cards when gap analysis data exists
  if (gapAnalysis) {
    const grade = gapAnalysis.grade || 'F';
    cards.push({
      label: 'ESI NOTU',
      value: grade,
      color: ESI_GRADE_COLORS[grade] || 'text-slate-400',
    });
    if (gapAnalysis.annual_bat_gap_cost_eur != null) {
      cards.push({
        label: 'BAT GAP',
        value: formatCurrency(gapAnalysis.annual_bat_gap_cost_eur),
        color: 'text-amber-400',
      });
    }
  }

  return (
    <div className="bg-slate-800 rounded-xl px-4 py-4 flex items-stretch gap-0 overflow-x-auto">
      {cards.map((card, i) => (
        <div
          key={card.label}
          className={`flex-1 min-w-[130px] flex flex-col items-center justify-center py-2 px-4 ${
            card.highlight ? 'bg-emerald-900/30 rounded-lg' : ''
          } ${i < cards.length - 1 ? 'border-r border-slate-700' : ''}`}
        >
          <span className="text-xs uppercase tracking-wider text-slate-400 mb-1">
            {card.label}
          </span>
          <span className={`font-mono font-bold text-2xl tabular-nums ${card.color}`}>
            {card.value}
          </span>
        </div>
      ))}
    </div>
  );
};

export default FactoryMetricBar;
