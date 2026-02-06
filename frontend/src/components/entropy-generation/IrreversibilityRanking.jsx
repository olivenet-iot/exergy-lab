import { Wind, Flame, Snowflake, Droplets, ArrowLeftRight, Zap, Sun, AlertTriangle } from 'lucide-react';
import { formatNumber } from '../../utils/formatters';

const GRADE_STYLES = {
  A: 'bg-green-100 text-green-700',
  B: 'bg-lime-100 text-lime-700',
  C: 'bg-amber-100 text-amber-700',
  D: 'bg-red-100 text-red-700',
  F: 'bg-red-200 text-red-900',
};

const MECHANISM_LABELS = {
  heat_transfer: 'DeltaT',
  pressure_drop: 'DeltaP',
  mixing: 'Karışma',
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

const IrreversibilityRanking = ({ ranking }) => {
  if (!ranking || ranking.length === 0) {
    return (
      <div className="text-center py-6 text-gray-500 text-sm">
        Siralama verisi yok
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
            {/* Grade badge */}
            <span className={`inline-flex items-center px-1.5 py-0.5 rounded text-xs font-bold flex-shrink-0 ${GRADE_STYLES[item.N_s_grade] || ''}`}>
              {item.N_s_grade}
            </span>

            {/* Icon + Name */}
            <Icon className="w-4 h-4 text-gray-400 flex-shrink-0" />
            <span className="font-medium text-gray-900 truncate flex-1">
              {item.equipment_name}
            </span>

            {/* Dominant mechanism */}
            <span className="text-xs text-gray-500 flex-shrink-0">
              {MECHANISM_LABELS[item.dominant_mechanism] || item.dominant_mechanism}
            </span>

            {/* N_s value */}
            <div className="flex-shrink-0 text-right">
              <div className="text-sm font-semibold text-purple-600">
                {formatNumber(item.N_s, 3)}
              </div>
              <div className="text-xs text-gray-500">N_s</div>
            </div>

            {/* Improvement potential */}
            <div className="flex-shrink-0 text-right w-14">
              <div className="text-sm font-mono text-green-600">
                {formatNumber(item.improvement_potential_pct, 0)}%
              </div>
              <div className="text-xs text-gray-400">potansiyel</div>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default IrreversibilityRanking;
