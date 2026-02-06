import { Gauge, Zap, CheckCircle, XCircle } from 'lucide-react';

const ICONS = {
  gauge: Gauge,
  zap: Zap,
  'check-circle': CheckCircle,
  'x-circle': XCircle,
};

const RATING_COLORS = {
  excellent: 'bg-green-100 text-green-800 border-green-200',
  good: 'bg-blue-100 text-blue-800 border-blue-200',
  average: 'bg-amber-100 text-amber-800 border-amber-200',
  poor: 'bg-red-100 text-red-800 border-red-200',
};

const RATING_LABELS = {
  excellent: 'Mükemmel',
  good: 'İyi',
  average: 'Ortalama',
  poor: 'Düşük',
};

const MetricsCard = ({ title, value, unit, rating, icon }) => {
  const Icon = ICONS[icon];

  return (
    <div className="bg-white rounded-xl border border-gray-200 p-4">
      <div className="flex items-center justify-between mb-2">
        <span className="text-sm text-gray-500">{title}</span>
        {Icon && <Icon className="w-5 h-5 text-gray-400" />}
      </div>

      <div className="flex items-baseline gap-1">
        <span className="text-2xl font-bold font-mono">
          {typeof value === 'number' ? value.toFixed(2) : value}
        </span>
        <span className="text-gray-500">{unit}</span>
      </div>

      {rating && (
        <div className={`
          inline-block mt-2 px-2 py-0.5 rounded text-xs font-medium
          ${RATING_COLORS[rating] || ''}
        `}>
          {RATING_LABELS[rating] || rating}
        </div>
      )}
    </div>
  );
};

export default MetricsCard;
