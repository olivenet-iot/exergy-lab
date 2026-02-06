import { useRef } from 'react';
import { Sparkles, AlertTriangle, Lightbulb, Clock, TrendingUp, XCircle } from 'lucide-react';
import Card from '../common/Card';
import AIActionBar from '../common/AIActionBar';
import { formatCurrency, formatNumber } from '../../utils/formatters';
import { PRIORITY_STYLES, PRIORITY_LABELS, PRIORITY_BADGE } from '../../utils/priorityStyles';

const AIInterpretation = ({ interpretation, loading }) => {
  const contentRef = useRef(null);

  if (loading) {
    return (
      <Card>
        <div className="flex items-center gap-3 py-8 justify-center">
          <Sparkles className="w-5 h-5 text-purple-500 animate-pulse" />
          <span className="text-gray-600">AI yorumu hazırlanıyor...</span>
        </div>
      </Card>
    );
  }

  if (!interpretation) return null;

  const {
    summary,
    detailed_analysis,
    key_insights = [],
    recommendations = [],
    not_recommended = [],
    action_plan = {},
    warnings = [],
  } = interpretation;

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Sparkles className="w-5 h-5 text-purple-500" />
          <h3 className="text-lg font-semibold text-gray-900">AI Yorumu</h3>
          <span className="px-2 py-0.5 rounded text-xs font-medium bg-purple-100 text-purple-700">
            Claude Code
          </span>
        </div>
        <AIActionBar contentRef={contentRef} fileName="ekipman-ai-yorum" />
      </div>

      <div ref={contentRef}>
        {/* Summary */}
        {summary && (
          <Card>
            <p className="text-gray-700 leading-relaxed">{summary}</p>
          </Card>
        )}

        {/* Detailed Analysis */}
        {detailed_analysis && (
          <Card title="Detaylı Analiz">
            <p className="text-gray-600 leading-relaxed">{detailed_analysis}</p>
          </Card>
        )}

        {/* Key Insights */}
        {key_insights.length > 0 && (
          <Card title="Önemli Bulgular">
            <ul className="space-y-2">
              {key_insights.map((insight, i) => (
                <li key={i} className="flex items-start gap-2">
                  <Lightbulb className="w-4 h-4 text-amber-500 mt-0.5 shrink-0" />
                  <span className="text-gray-600">{insight}</span>
                </li>
              ))}
            </ul>
          </Card>
        )}

        {/* Recommendations */}
        {recommendations.length > 0 && (
          <div className="space-y-4">
            <h4 className="text-base font-semibold text-gray-900 flex items-center gap-2">
              <TrendingUp className="w-4 h-4" />
              Öneriler
            </h4>
            {recommendations.map((rec, i) => (
              <div
                key={i}
                className={`border-l-4 rounded-lg p-4 ${PRIORITY_STYLES[rec.priority] || 'border-l-gray-300 bg-gray-50'}`}
              >
                <div className="flex items-start justify-between">
                  <div>
                    <div className="flex items-center gap-2">
                      <h5 className="font-medium text-gray-900">{rec.title}</h5>
                      <span className={`px-2 py-0.5 rounded text-xs font-medium ${PRIORITY_BADGE[rec.priority] || ''}`}>
                        {PRIORITY_LABELS[rec.priority] || rec.priority}
                      </span>
                    </div>
                    <p className="text-sm text-gray-600 mt-1">{rec.description}</p>
                  </div>
                </div>

                <div className="mt-3 grid grid-cols-3 gap-4 text-sm">
                  <div>
                    <span className="text-gray-500">Yıllık Tasarruf</span>
                    <p className="font-semibold text-green-600">
                      {formatCurrency(rec.estimated_savings_eur_year)}
                    </p>
                  </div>
                  <div>
                    <span className="text-gray-500">Tahmini Yatırım</span>
                    <p className="font-semibold">
                      {formatCurrency(rec.estimated_investment_eur)}
                    </p>
                  </div>
                  <div>
                    <span className="text-gray-500">Geri Ödeme</span>
                    <p className="font-semibold">
                      {formatNumber(rec.payback_years, 1)} yıl
                    </p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Not Recommended */}
        {not_recommended.length > 0 && (
          <Card title="Önerilmeyen Çözümler">
            <div className="space-y-3">
              {not_recommended.map((item, i) => (
                <div key={i} className="flex items-start gap-2">
                  <XCircle className="w-4 h-4 text-gray-400 mt-0.5 shrink-0" />
                  <div>
                    <span className="font-medium text-gray-700">{item.title}</span>
                    <p className="text-sm text-gray-500">{item.reason}</p>
                  </div>
                </div>
              ))}
            </div>
          </Card>
        )}

        {/* Action Plan */}
        {(action_plan.immediate?.length > 0 || action_plan.short_term?.length > 0 || action_plan.medium_term?.length > 0) && (
          <Card title="Aksiyon Plani">
            <div className="space-y-4">
              {action_plan.immediate?.length > 0 && (
                <div>
                  <div className="flex items-center gap-2 mb-2">
                    <Clock className="w-4 h-4 text-red-500" />
                    <span className="text-sm font-medium text-gray-700">Hemen</span>
                  </div>
                  <ul className="ml-6 space-y-1">
                    {action_plan.immediate.map((item, i) => (
                      <li key={i} className="text-sm text-gray-600 list-disc">{item}</li>
                    ))}
                  </ul>
                </div>
              )}

              {action_plan.short_term?.length > 0 && (
                <div>
                  <div className="flex items-center gap-2 mb-2">
                    <Clock className="w-4 h-4 text-amber-500" />
                    <span className="text-sm font-medium text-gray-700">Kısa Vade (1-3 ay)</span>
                  </div>
                  <ul className="ml-6 space-y-1">
                    {action_plan.short_term.map((item, i) => (
                      <li key={i} className="text-sm text-gray-600 list-disc">{item}</li>
                    ))}
                  </ul>
                </div>
              )}

              {action_plan.medium_term?.length > 0 && (
                <div>
                  <div className="flex items-center gap-2 mb-2">
                    <Clock className="w-4 h-4 text-blue-500" />
                    <span className="text-sm font-medium text-gray-700">Orta Vade (3-12 ay)</span>
                  </div>
                  <ul className="ml-6 space-y-1">
                    {action_plan.medium_term.map((item, i) => (
                      <li key={i} className="text-sm text-gray-600 list-disc">{item}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </Card>
        )}

        {/* Warnings */}
        {warnings.length > 0 && (
          <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <AlertTriangle className="w-4 h-4 text-amber-600" />
              <span className="text-sm font-medium text-amber-800">Uyarılar</span>
            </div>
            <ul className="space-y-1">
              {warnings.map((warning, i) => (
                <li key={i} className="text-sm text-amber-700">{warning}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};

export default AIInterpretation;
