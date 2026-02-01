import { ArrowRight, Zap } from 'lucide-react';
import Card from '../common/Card';
import { formatCurrency, formatNumber } from '../../utils/formatters';

const COMPLEXITY_STYLES = {
  low: 'bg-green-100 text-green-700',
  medium: 'bg-amber-100 text-amber-700',
  high: 'bg-red-100 text-red-700',
};

const COMPLEXITY_LABELS = {
  low: 'Kolay',
  medium: 'Orta',
  high: 'Karmasik',
};

const IntegrationOpportunities = ({ opportunities }) => {
  if (!opportunities || opportunities.length === 0) return null;

  return (
    <div className="space-y-4">
      <h3 className="text-lg font-semibold text-gray-900 flex items-center gap-2">
        <Zap className="w-5 h-5 text-amber-500" />
        Entegrasyon Firsatlari
      </h3>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {opportunities.map((opp, index) => (
          <div
            key={index}
            className="bg-white rounded-xl border border-gray-200 p-5 hover:border-amber-300 transition-colors"
          >
            {/* Title */}
            <h4 className="font-medium text-gray-900 mb-2">{opp.title}</h4>

            {/* Source -> Target */}
            <div className="flex items-center gap-2 mb-3 text-sm">
              <span className="px-2 py-1 bg-blue-50 text-blue-700 rounded font-medium">{opp.source}</span>
              <ArrowRight className="w-4 h-4 text-gray-400" />
              <span className="px-2 py-1 bg-green-50 text-green-700 rounded font-medium">{opp.target}</span>
            </div>

            {/* Description */}
            <p className="text-sm text-gray-600 mb-3">{opp.description}</p>

            {/* Metrics */}
            <div className="grid grid-cols-2 gap-3 text-sm">
              <div>
                <span className="text-gray-500">Geri Kazanim</span>
                <p className="font-semibold text-gray-900">{formatNumber(opp.potential_recovery_kW, 1)} kW</p>
              </div>
              <div>
                <span className="text-gray-500">Yillik Tasarruf</span>
                <p className="font-semibold text-green-600">{formatCurrency(opp.estimated_savings_EUR_year)}</p>
              </div>
              <div>
                <span className="text-gray-500">Yatirim</span>
                <p className="font-semibold text-gray-900">{formatCurrency(opp.estimated_investment_EUR)}</p>
              </div>
              <div>
                <span className="text-gray-500">ROI</span>
                <p className="font-semibold text-gray-900">{formatNumber(opp.roi_years, 1)} yil</p>
              </div>
            </div>

            {/* Complexity badge */}
            <div className="mt-3">
              <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium ${COMPLEXITY_STYLES[opp.complexity] || 'bg-gray-100 text-gray-600'}`}>
                Karmasiklik: {COMPLEXITY_LABELS[opp.complexity] || opp.complexity}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default IntegrationOpportunities;
