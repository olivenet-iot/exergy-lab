import { ArrowRight } from 'lucide-react';
import { formatNumber } from '../../utils/formatters';

const HENMatches = ({ matches }) => {
  if (!matches || matches.length === 0) {
    return (
      <div className="text-center py-4 text-gray-400 text-sm">
        HEN eşleştirmesi bulunamadı
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {matches.map((m, i) => (
        <div
          key={i}
          className="flex items-center gap-3 p-3 bg-gray-50 rounded-lg border border-gray-100"
        >
          {/* Hot side */}
          <div className="flex-1 text-right">
            <div className="text-sm font-medium text-red-700">
              {m.hot_equipment}
            </div>
            <div className="text-xs text-gray-500">
              {formatNumber(m.T_hot_supply_C, 0)}°C
            </div>
          </div>

          {/* Arrow + Q */}
          <div className="flex flex-col items-center px-2">
            <ArrowRight className="w-4 h-4 text-gray-400" />
            <span className="text-xs font-mono font-semibold text-gray-700 mt-0.5">
              {formatNumber(m.Q_exchange_kW, 1)} kW
            </span>
          </div>

          {/* Cold side */}
          <div className="flex-1">
            <div className="text-sm font-medium text-blue-700">
              {m.cold_equipment}
            </div>
            <div className="text-xs text-gray-500">
              {formatNumber(m.T_cold_target_C, 0)}°C
            </div>
          </div>

          {/* Region badge */}
          <span className="text-xs px-1.5 py-0.5 rounded bg-gray-200 text-gray-600">
            {m.region === 'above_pinch' ? 'Pinch üstü' : m.region === 'below_pinch' ? 'Pinch altı' : 'Tüm'}
          </span>
        </div>
      ))}
    </div>
  );
};

export default HENMatches;
