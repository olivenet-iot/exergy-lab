import { Sparkles, AlertTriangle, TrendingUp, Lightbulb, Target, Globe } from 'lucide-react';
import Card from '../common/Card';
import { formatCurrency, formatNumber } from '../../utils/formatters';
import { PRIORITY_STYLES, PRIORITY_BADGE, PRIORITY_LABELS } from '../../utils/priorityStyles';

const FactoryAIInterpretation = ({ interpretation, loading }) => {
  if (loading) {
    return (
      <Card>
        <div className="flex items-center gap-3 py-8 justify-center">
          <Sparkles className="w-5 h-5 text-purple-500 animate-pulse" />
          <span className="text-gray-600">Fabrika AI yorumu hazırlanıyor...</span>
        </div>
      </Card>
    );
  }

  if (!interpretation) return null;
  if (interpretation.ai_available === false) return null;

  const {
    summary,
    hotspot_analysis = [],
    integration_opportunities = [],
    prioritized_actions = [],
    sector_specific_insights = [],
    warnings = [],
  } = interpretation;

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center gap-2">
        <Sparkles className="w-5 h-5 text-purple-500" />
        <h3 className="text-lg font-semibold text-gray-900">Fabrika AI Yorumu</h3>
        <span className="px-2 py-0.5 rounded text-xs font-medium bg-purple-100 text-purple-700">
          Claude Code
        </span>
      </div>

      {/* Summary */}
      {summary && (
        <Card>
          <p className="text-gray-700 leading-relaxed">{summary}</p>
        </Card>
      )}

      {/* Hotspot Analysis */}
      {hotspot_analysis.length > 0 && (
        <Card title="Hotspot Analizi">
          <div className="space-y-3">
            {hotspot_analysis.map((h, i) => (
              <div key={i} className="flex items-start gap-3 p-3 rounded-lg bg-gray-50">
                <Target className="w-4 h-4 text-red-500 mt-0.5 shrink-0" />
                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-medium text-gray-900">{h.equipment_name}</span>
                    <span className={`px-1.5 py-0.5 rounded text-xs font-medium ${PRIORITY_BADGE[h.priority] || ''}`}>
                      {PRIORITY_LABELS[h.priority] || h.priority}
                    </span>
                  </div>
                  <p className="text-sm text-gray-600 mt-0.5">{h.finding}</p>
                  {h.exergy_destroyed_kW && (
                    <span className="text-xs text-gray-500">Exergy yıkımı: {formatNumber(h.exergy_destroyed_kW, 1)} kW</span>
                  )}
                </div>
              </div>
            ))}
          </div>
        </Card>
      )}

      {/* Integration Opportunities */}
      {integration_opportunities.length > 0 && (
        <Card title="Entegrasyon Fırsatları">
          <div className="space-y-3">
            {integration_opportunities.map((opp, i) => (
              <div key={i} className="flex items-start gap-3 p-3 rounded-lg bg-gray-50">
                <Lightbulb className="w-4 h-4 text-amber-500 mt-0.5 shrink-0" />
                <div>
                  <span className="font-medium text-gray-900">{opp.title}</span>
                  <p className="text-sm text-gray-600 mt-0.5">{opp.description}</p>
                  {opp.potential_savings_eur_year && (
                    <span className="text-xs text-green-600 font-medium">
                      Tasarruf: {formatCurrency(opp.potential_savings_eur_year)}/yıl
                    </span>
                  )}
                </div>
              </div>
            ))}
          </div>
        </Card>
      )}

      {/* Prioritized Actions */}
      {prioritized_actions.length > 0 && (
        <div className="space-y-4">
          <h4 className="text-base font-semibold text-gray-900 flex items-center gap-2">
            <TrendingUp className="w-4 h-4" />
            Öncelikli Aksiyonlar
          </h4>
          {prioritized_actions.map((action, i) => (
            <div
              key={i}
              className={`border-l-4 rounded-lg p-4 ${PRIORITY_STYLES[action.priority] || 'border-l-gray-300 bg-gray-50'}`}
            >
              <div className="flex items-center gap-2 mb-1">
                <span className="text-sm font-bold text-gray-500">#{action.rank || i + 1}</span>
                <h5 className="font-medium text-gray-900">{action.action}</h5>
                <span className={`px-2 py-0.5 rounded text-xs font-medium ${PRIORITY_BADGE[action.priority] || ''}`}>
                  {PRIORITY_LABELS[action.priority] || action.priority}
                </span>
              </div>

              <div className="mt-2 grid grid-cols-3 gap-4 text-sm">
                <div>
                  <span className="text-gray-500">Yıllık Tasarruf</span>
                  <p className="font-semibold text-green-600">
                    {formatCurrency(action.estimated_savings_eur_year)}
                  </p>
                </div>
                <div>
                  <span className="text-gray-500">Yatırım</span>
                  <p className="font-semibold">
                    {formatCurrency(action.estimated_investment_eur)}
                  </p>
                </div>
                <div>
                  <span className="text-gray-500">Geri Ödeme</span>
                  <p className="font-semibold">
                    {formatNumber(action.payback_years, 1)} yıl
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Sector-Specific Insights */}
      {sector_specific_insights.length > 0 && (
        <Card title="Sektöre Özel Bulgular">
          <ul className="space-y-2">
            {sector_specific_insights.map((insight, i) => (
              <li key={i} className="flex items-start gap-2">
                <Globe className="w-4 h-4 text-cyan-500 mt-0.5 shrink-0" />
                <span className="text-gray-600">{insight}</span>
              </li>
            ))}
          </ul>
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
  );
};

export default FactoryAIInterpretation;
