import { ArrowRight } from 'lucide-react';
import { formatNumber } from '../../utils/formatters';

const InteractionNetwork = ({ edges }) => {
  if (!edges || edges.length === 0) {
    return (
      <div className="text-center py-6 text-gray-500 text-sm">
        Ekipmanlar arası etkileşim tespit edilmedi
      </div>
    );
  }

  const maxValue = Math.max(...edges.map((e) => e.value_kW));

  return (
    <div className="space-y-2">
      {edges.map((edge, index) => {
        const intensity = maxValue > 0 ? edge.value_kW / maxValue : 0;
        const bgOpacity = Math.max(0.1, intensity * 0.3);

        return (
          <div
            key={`${edge.source_id}-${edge.target_id}-${index}`}
            className="flex items-center gap-2 p-2 rounded-lg border border-gray-200 text-sm"
            style={{ backgroundColor: `rgba(245, 158, 11, ${bgOpacity})` }}
          >
            <span className="font-medium text-gray-800 truncate flex-1">
              {edge.source}
            </span>
            <ArrowRight className="w-3 h-3 text-amber-600 flex-shrink-0" />
            <span className="font-medium text-gray-800 truncate flex-1">
              {edge.target}
            </span>
            <span className="font-mono font-semibold text-amber-700 flex-shrink-0">
              {formatNumber(edge.value_kW, 1)} kW
            </span>
          </div>
        );
      })}
    </div>
  );
};

export default InteractionNetwork;
