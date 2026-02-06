import { Sparkles } from 'lucide-react';

const AIInsightCard = ({ summary, topRecommendation, onViewDetails, loading }) => {
  if (loading) {
    return (
      <div className="bg-gradient-to-r from-violet-50 to-blue-50 border border-violet-200 rounded-xl p-5">
        <div className="flex items-center gap-3 animate-pulse">
          <Sparkles className="w-5 h-5 text-violet-400" />
          <div className="flex-1 space-y-2">
            <div className="h-4 bg-violet-200/50 rounded w-3/4" />
            <div className="h-3 bg-violet-200/50 rounded w-1/2" />
          </div>
        </div>
      </div>
    );
  }

  if (!summary) return null;

  return (
    <div className="bg-gradient-to-r from-violet-50 to-blue-50 border border-violet-200 rounded-xl p-5">
      <div className="flex items-start gap-3">
        <Sparkles className="w-5 h-5 text-violet-600 mt-0.5 shrink-0" />
        <div className="flex-1 min-w-0">
          <p className="text-gray-700 leading-relaxed">{summary}</p>

          {topRecommendation && (
            <div className="mt-3 flex items-center gap-2 text-sm">
              <span className="text-violet-600 font-medium">En onemli oneri:</span>
              <span className="text-gray-600 truncate">{topRecommendation.title}</span>
              {topRecommendation.estimated_savings_eur_year > 0 && (
                <span className="text-emerald-600 font-mono text-xs whitespace-nowrap">
                  +{Math.round(topRecommendation.estimated_savings_eur_year).toLocaleString('tr-TR')} EUR/yil
                </span>
              )}
            </div>
          )}

          {onViewDetails && (
            <button
              onClick={onViewDetails}
              className="mt-3 text-sm text-violet-600 hover:text-violet-700 font-medium"
            >
              Detayli AI yorumunu oku &rarr;
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default AIInsightCard;
