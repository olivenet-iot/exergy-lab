import { ArrowRight, Zap } from 'lucide-react';
import { formatCurrency, formatNumber } from '../../utils/formatters';

const COMPLEXITY_STYLES = {
  low: 'bg-green-100 text-green-700',
  medium: 'bg-amber-100 text-amber-700',
  high: 'bg-red-100 text-red-700',
};

const COMPLEXITY_LABELS = {
  low: 'Kolay',
  medium: 'Orta',
  high: 'Karmaşık',
};

const IntegrationPanel = ({ opportunities }) => {
  if (!opportunities || opportunities.length === 0) {
    return (
      <div className="text-center py-6 text-gray-400">
        Entegrasyon fırsatı tespit edilmedi
      </div>
    );
  }

  const totalSavings = opportunities.reduce(
    (sum, opp) => sum + (opp.estimated_savings_EUR_year || 0),
    0
  );

  return (
    <div className="space-y-3">
      {opportunities.map((opp, index) => (
        <div
          key={index}
          className="p-3 rounded-lg border border-gray-200 hover:border-amber-300 transition-colors"
        >
          <h4 className="font-medium text-gray-900 text-sm mb-2">{opp.title}</h4>

          {/* Source -> Target */}
          <div className="flex items-center gap-1.5 mb-2 text-xs">
            <span className="px-1.5 py-0.5 bg-blue-50 text-blue-700 rounded font-medium truncate">
              {opp.source}
            </span>
            <ArrowRight className="w-3 h-3 text-gray-400 flex-shrink-0" />
            <span className="px-1.5 py-0.5 bg-green-50 text-green-700 rounded font-medium truncate">
              {opp.target}
            </span>
          </div>

          {/* Metrics row */}
          <div className="flex items-center justify-between text-xs">
            <span className="text-gray-500">
              {formatNumber(opp.potential_recovery_kW, 1)} kW
            </span>
            <span className="font-semibold text-green-600">
              {formatCurrency(opp.estimated_savings_EUR_year)}/yıl
            </span>
            <span className={`px-1.5 py-0.5 rounded font-medium ${COMPLEXITY_STYLES[opp.complexity] || 'bg-gray-100 text-gray-600'}`}>
              {COMPLEXITY_LABELS[opp.complexity] || opp.complexity}
            </span>
          </div>
        </div>
      ))}

      {/* Total potential summary footer */}
      <div className="bg-green-50 rounded-lg p-3 flex items-center justify-between">
        <div>
          <span className="text-xs uppercase tracking-wider text-green-700 font-medium">
            TOPLAM POTANSİYEL
          </span>
          <span className="text-xs text-green-600 ml-2">
            ({opportunities.length} fırsat)
          </span>
        </div>
        <span className="font-mono font-semibold text-green-700">
          {formatCurrency(totalSavings)}/yıl
        </span>
      </div>
    </div>
  );
};

export default IntegrationPanel;
