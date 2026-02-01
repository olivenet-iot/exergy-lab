import { AlertTriangle, Wind, Flame, Snowflake, Droplets } from 'lucide-react';
import { formatNumber, formatCurrency } from '../../utils/formatters';

const PRIORITY_STYLES = {
  high: 'bg-red-100 text-red-700',
  medium: 'bg-amber-100 text-amber-700',
  low: 'bg-blue-100 text-blue-700',
};

const PRIORITY_LABELS = {
  high: 'Yuksek',
  medium: 'Orta',
  low: 'Dusuk',
};

const EQUIPMENT_ICONS = {
  compressor: Wind,
  boiler: Flame,
  chiller: Snowflake,
  pump: Droplets,
};

const HotspotList = ({ hotspots }) => {
  if (!hotspots || hotspots.length === 0) return null;

  return (
    <div className="space-y-3">
      {hotspots.map((hotspot, index) => {
        const Icon = EQUIPMENT_ICONS[hotspot.equipment_type] || AlertTriangle;

        return (
          <div
            key={hotspot.id || index}
            className="flex items-center gap-4 p-3 rounded-lg border border-gray-200 hover:border-gray-300 transition-colors"
          >
            {/* Rank */}
            <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center text-sm font-bold text-gray-600">
              {index + 1}
            </div>

            {/* Icon */}
            <Icon className="w-5 h-5 text-gray-400 flex-shrink-0" />

            {/* Info */}
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2">
                <span className="font-medium text-gray-900 truncate">{hotspot.name}</span>
                <span className={`inline-flex items-center px-1.5 py-0.5 rounded text-xs font-medium ${PRIORITY_STYLES[hotspot.priority] || ''}`}>
                  {PRIORITY_LABELS[hotspot.priority] || hotspot.priority}
                </span>
              </div>
              <div className="text-xs text-gray-500 mt-0.5">
                {hotspot.subtype} — Verim: {formatNumber(hotspot.exergy_efficiency_pct, 1)}%
              </div>
            </div>

            {/* Metrics */}
            <div className="flex-shrink-0 text-right">
              <div className="text-sm font-semibold text-red-600">
                {formatNumber(hotspot.exergy_destroyed_kW, 1)} kW
              </div>
              <div className="text-xs text-gray-500">
                {formatCurrency(hotspot.annual_loss_EUR)}/yil
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default HotspotList;
