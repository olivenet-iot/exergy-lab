import { Wind, Flame, Snowflake, Droplets, ArrowLeftRight, Zap, Sun, AlertTriangle } from 'lucide-react';
import { formatNumber } from '../../utils/formatters';

const PRIORITY_STYLES = {
  high: 'bg-red-100 text-red-700',
  medium: 'bg-amber-100 text-amber-700',
  low: 'bg-green-100 text-green-700',
};

const PRIORITY_LABELS = {
  high: 'Yüksek',
  medium: 'Orta',
  low: 'Düşük',
};

const EQUIPMENT_ICONS = {
  compressor: Wind,
  boiler: Flame,
  chiller: Snowflake,
  pump: Droplets,
  heat_exchanger: ArrowLeftRight,
  steam_turbine: Zap,
  dryer: Sun,
};

const AdvancedExergyPriorityList = ({ ranking }) => {
  if (!ranking || ranking.length === 0) {
    return (
      <div className="text-center py-6 text-gray-500 text-sm">
        Öncelik verisi yok
      </div>
    );
  }

  return (
    <div className="space-y-2">
      {ranking.map((item, index) => {
        const Icon = EQUIPMENT_ICONS[item.equipment_type] || AlertTriangle;

        return (
          <div
            key={item.equipment_id || index}
            className="flex items-center gap-3 p-3 rounded-lg border border-gray-200 hover:bg-slate-50 transition-colors"
          >
            {/* Priority badge */}
            <span className={`inline-flex items-center px-1.5 py-0.5 rounded text-xs font-medium flex-shrink-0 ${PRIORITY_STYLES[item.priority] || ''}`}>
              {PRIORITY_LABELS[item.priority] || item.priority}
            </span>

            {/* Icon + Name */}
            <Icon className="w-4 h-4 text-gray-400 flex-shrink-0" />
            <span className="font-medium text-gray-900 truncate flex-1">
              {item.equipment_name}
            </span>

            {/* AV-EN value */}
            <div className="flex-shrink-0 text-right">
              <div className="text-sm font-semibold text-green-600">
                {formatNumber(item.I_AV_EN_kW, 1)} kW
              </div>
              <div className="text-xs text-gray-500">AV-EN</div>
            </div>

            {/* Isolation factor */}
            <div className="flex-shrink-0 text-right w-14">
              <div className="text-sm font-mono text-gray-700">
                {formatNumber(item.isolation_factor, 2)}
              </div>
              <div className="text-xs text-gray-400">&phi;</div>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default AdvancedExergyPriorityList;
