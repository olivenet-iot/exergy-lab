import { AlertTriangle, Wind, Flame, Snowflake, Droplets, ArrowLeftRight, Zap, Sun } from 'lucide-react';
import { formatNumber, formatCurrency } from '../../utils/formatters';

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

const GRADE_COLORS = {
  A: 'text-green-600 bg-green-50',
  B: 'text-cyan-600 bg-cyan-50',
  C: 'text-amber-600 bg-amber-50',
  D: 'text-orange-600 bg-orange-50',
  F: 'text-red-600 bg-red-50',
};

const PriorityList = ({ hotspots, equipmentResults, totalDestroyed, onEquipmentClick }) => {
  if (!hotspots || hotspots.length === 0) {
    return (
      <div className="text-center py-6 text-gray-500">
        Henüz ekipman analizi yapılmadı
      </div>
    );
  }

  return (
    <div className="space-y-2">
      {hotspots.map((hotspot, index) => {
        const Icon = EQUIPMENT_ICONS[hotspot.equipment_type] || AlertTriangle;
        const efficiency = hotspot.exergy_efficiency_pct;
        const effColor =
          efficiency >= 70
            ? 'bg-green-500'
            : efficiency >= 50
              ? 'bg-amber-500'
              : 'bg-red-500';

        const share = totalDestroyed > 0
          ? ((hotspot.exergy_destroyed_kW / totalDestroyed) * 100).toFixed(1)
          : 0;

        // Look up equipment result for AV/UN and radar data
        const eqResult = equipmentResults?.find(r => r.id === hotspot.id);
        const avoidable = eqResult?.analysis?.exergy_destroyed_avoidable_kW;
        const unavoidable = eqResult?.analysis?.exergy_destroyed_unavoidable_kW;
        const hasAvUn = avoidable != null && unavoidable != null;
        const avTotal = hasAvUn ? avoidable + unavoidable : 0;
        const avPct = avTotal > 0 ? (avoidable / avTotal) * 100 : 0;

        const gradeLetter = eqResult?.analysis?.radar_data?.grade_letter;
        const gradeStyle = gradeLetter ? GRADE_COLORS[gradeLetter] || 'text-slate-600 bg-slate-50' : null;

        return (
          <div
            key={hotspot.id || index}
            onClick={() => onEquipmentClick?.(hotspot)}
            className="flex items-center gap-4 p-3 rounded-lg border border-gray-200 hover:bg-slate-50 cursor-pointer transition-colors"
          >
            {/* Priority + Icon + Name */}
            <div className="flex items-center gap-2 min-w-0 flex-1">
              <span className={`inline-flex items-center px-1.5 py-0.5 rounded text-xs font-medium ${PRIORITY_STYLES[hotspot.priority] || ''}`}>
                {PRIORITY_LABELS[hotspot.priority] || hotspot.priority}
              </span>
              <Icon className="w-4 h-4 text-gray-400 flex-shrink-0" />
              <span className="font-medium text-gray-900 truncate">{hotspot.name}</span>
              {hotspot.subtype && (
                <span className="text-xs text-gray-500 flex-shrink-0">{hotspot.subtype}</span>
              )}
            </div>

            {/* Efficiency bar */}
            <div className="flex items-center gap-2 flex-shrink-0 w-36">
              <div className="flex-1 h-2 bg-gray-200 rounded-full overflow-hidden">
                <div
                  className={`h-full rounded-full ${effColor}`}
                  style={{ width: `${Math.min(efficiency || 0, 100)}%` }}
                />
              </div>
              <span className="text-xs font-mono text-gray-600 w-10 text-right">
                %{formatNumber(efficiency)}
              </span>
            </div>

            {/* AV/UN mini-bar (conditional) */}
            {hasAvUn && (
              <div className="flex items-center gap-1 flex-shrink-0 w-20">
                <div className="flex-1 h-2 bg-gray-300 rounded-full overflow-hidden">
                  <div
                    className="h-full rounded-full bg-red-500"
                    style={{ width: `${avPct}%` }}
                  />
                </div>
                <span className="text-xs text-gray-500">AV</span>
              </div>
            )}

            {/* Radar grade badge (conditional) */}
            {gradeStyle && (
              <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-semibold ${gradeStyle}`}>
                {gradeLetter}
              </span>
            )}

            {/* Destruction metrics */}
            <div className="flex-shrink-0 text-right">
              <div className="text-sm font-semibold text-red-600">
                {formatNumber(hotspot.exergy_destroyed_kW, 1)} kW
                <span className="text-xs text-gray-500 ml-1">({share}%)</span>
              </div>
              <div className="text-xs text-gray-500">
                {formatCurrency(hotspot.annual_loss_EUR)}/yıl
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default PriorityList;
