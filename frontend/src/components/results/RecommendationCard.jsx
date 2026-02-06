import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import { PRIORITY_STYLES, PRIORITY_BADGE, PRIORITY_LABELS } from '../../utils/priorityStyles';
import { formatCurrency, formatNumber } from '../../utils/formatters';

const RecommendationCard = ({ rec, index, defaultOpen = false }) => {
  const [isOpen, setIsOpen] = useState(defaultOpen);

  const savings = rec.estimated_savings_eur_year;
  const investment = rec.estimated_investment_eur;
  const payback = rec.payback_years;

  return (
    <div
      className={`border-l-4 rounded-lg overflow-hidden ${PRIORITY_STYLES[rec.priority] || 'border-l-gray-300 bg-gray-50'}`}
    >
      {/* Header — always visible */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full text-left px-4 py-3 flex items-center gap-3"
      >
        {/* Index */}
        <span className="flex-shrink-0 w-6 h-6 rounded-full bg-white/70 flex items-center justify-center text-xs font-bold text-gray-700">
          {index + 1}
        </span>

        {/* Title + Priority */}
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 flex-wrap">
            <h5 className="font-medium text-gray-900 truncate">{rec.title}</h5>
            <span className={`px-2 py-0.5 rounded text-xs font-medium whitespace-nowrap ${PRIORITY_BADGE[rec.priority] || ''}`}>
              {PRIORITY_LABELS[rec.priority] || rec.priority}
            </span>
          </div>
        </div>

        {/* Mini KPI badges */}
        <div className="hidden sm:flex items-center gap-2 flex-shrink-0">
          {savings > 0 && (
            <span className="text-xs font-mono tabular-nums text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded">
              +{formatCurrency(savings)}/y
            </span>
          )}
          {investment > 0 && (
            <span className="text-xs font-mono tabular-nums text-gray-600 bg-white/70 px-2 py-0.5 rounded">
              {formatCurrency(investment)}
            </span>
          )}
          {payback > 0 && (
            <span className="text-xs font-mono tabular-nums text-blue-700 bg-blue-50 px-2 py-0.5 rounded">
              {formatNumber(payback, 1)}y
            </span>
          )}
        </div>

        {/* Chevron */}
        <ChevronDown
          className={`w-4 h-4 text-gray-400 transition-transform duration-200 flex-shrink-0 ${isOpen ? 'rotate-180' : ''}`}
        />
      </button>

      {/* Body — collapsible */}
      <div
        className="overflow-hidden transition-all duration-300 ease-in-out"
        style={{ maxHeight: isOpen ? '500px' : '0px' }}
      >
        <div className="px-4 pb-4 pt-0">
          <p className="text-sm text-gray-600 leading-relaxed">{rec.description}</p>

          {/* Financial details on mobile */}
          <div className="mt-3 grid grid-cols-3 gap-4 text-sm sm:hidden">
            <div>
              <span className="text-gray-500 text-xs">Tasarruf</span>
              <p className="font-semibold text-green-600">{formatCurrency(savings)}</p>
            </div>
            <div>
              <span className="text-gray-500 text-xs">Yatırım</span>
              <p className="font-semibold">{formatCurrency(investment)}</p>
            </div>
            <div>
              <span className="text-gray-500 text-xs">Geri Ödeme</span>
              <p className="font-semibold">{formatNumber(payback, 1)} yıl</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RecommendationCard;
