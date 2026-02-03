import { formatNumber } from '../../utils/formatters';

const GRADE_COLORS = {
  A: 'text-green-600 bg-green-50',
  B: 'text-cyan-600 bg-cyan-50',
  C: 'text-amber-600 bg-amber-50',
  D: 'text-orange-600 bg-orange-50',
  F: 'text-red-600 bg-red-50',
};

const MetricBar = ({ metrics, radarData }) => {
  if (!metrics) return null;

  const efficiency = metrics.exergy_efficiency_percent;
  const destroyed = metrics.exergy_destroyed_kW;
  const avoidableRatio = metrics.avoidable_ratio_pct;
  const annualCost = metrics.annual_cost_eur;
  const gradeLetter = radarData?.grade_letter;
  const overallScore = radarData?.overall_score;

  const effColor =
    efficiency >= 70
      ? 'text-green-600'
      : efficiency >= 50
        ? 'text-amber-600'
        : 'text-red-600';

  const avColor =
    avoidableRatio == null
      ? 'text-slate-400'
      : avoidableRatio <= 25
        ? 'text-green-600'
        : avoidableRatio <= 50
          ? 'text-amber-600'
          : 'text-red-600';

  const gradeStyle = gradeLetter ? GRADE_COLORS[gradeLetter] || 'text-slate-600 bg-slate-50' : '';

  const cards = [
    {
      label: 'VERİM',
      value: efficiency != null ? `%${formatNumber(efficiency)}` : '—',
      color: efficiency != null ? effColor : 'text-slate-400',
    },
    {
      label: 'YIKIM',
      value: destroyed != null ? `${formatNumber(destroyed)} kW` : '—',
      color: 'text-red-600',
    },
    {
      label: 'KAÇINILABİLİR',
      value: avoidableRatio != null ? `%${formatNumber(avoidableRatio)}` : '—',
      color: avColor,
    },
    {
      label: 'YILLIK KAYIP',
      value: annualCost != null ? `€${formatNumber(annualCost, 0)}` : '—',
      color: annualCost != null ? 'text-red-600' : 'text-slate-400',
    },
    {
      label: 'NOT',
      value: gradeLetter ? `${gradeLetter} (${overallScore})` : '—',
      color: gradeLetter ? '' : 'text-slate-400',
      badge: gradeStyle,
    },
  ];

  return (
    <div className="flex items-stretch gap-3 px-6 py-3 bg-white border-b border-slate-200 overflow-x-auto">
      {cards.map((card) => (
        <div
          key={card.label}
          className="flex-1 min-w-[120px] flex flex-col items-center justify-center py-2 px-3 rounded-lg bg-slate-50"
        >
          <span className="text-xs uppercase tracking-wider text-slate-500 mb-1">
            {card.label}
          </span>
          <span
            className={`font-mono font-semibold text-lg ${card.badge ? card.badge + ' px-2 py-0.5 rounded' : card.color}`}
          >
            {card.value}
          </span>
        </div>
      ))}
    </div>
  );
};

export default MetricBar;
