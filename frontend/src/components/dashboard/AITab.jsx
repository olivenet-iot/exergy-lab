import { useState, useRef } from 'react';
import { Sparkles, AlertTriangle, Lightbulb, TrendingUp, XCircle, ChevronDown } from 'lucide-react';
import Card from '../common/Card';
import AIActionBar from '../common/AIActionBar';
import RecommendationCard from '../results/RecommendationCard';
import ActionTimeline from '../results/ActionTimeline';

const CollapsibleSection = ({ title, icon: Icon, iconColor, defaultOpen = false, children }) => {
  const [isOpen, setIsOpen] = useState(defaultOpen);

  return (
    <div className="bg-white rounded-xl border border-gray-200 overflow-hidden">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full flex items-center justify-between px-5 py-4 hover:bg-gray-50 transition-colors"
      >
        <div className="flex items-center gap-2">
          {Icon && <Icon className={`w-4 h-4 ${iconColor || 'text-gray-500'}`} />}
          <span className="text-base font-semibold text-gray-900">{title}</span>
        </div>
        <ChevronDown
          className={`w-4 h-4 text-gray-400 transition-transform duration-200 ${isOpen ? 'rotate-180' : ''}`}
        />
      </button>
      <div
        className="overflow-hidden transition-all duration-300 ease-in-out"
        style={{ maxHeight: isOpen ? '2000px' : '0px' }}
      >
        <div className="px-5 pb-5">{children}</div>
      </div>
    </div>
  );
};

const AITab = ({ interpretation, aiLoading, equipmentType, subtype, result }) => {
  const contentRef = useRef(null);
  const [summaryExpanded, setSummaryExpanded] = useState(false);

  if (aiLoading) {
    return (
      <Card>
        <div className="flex items-center gap-3 py-8 justify-center">
          <Sparkles className="w-5 h-5 text-purple-500 animate-pulse" />
          <span className="text-gray-600">AI yorumu hazirlaniyor...</span>
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

  const hasActionPlan = action_plan.immediate?.length > 0 || action_plan.short_term?.length > 0 || action_plan.medium_term?.length > 0;

  return (
    <div className="space-y-6">
      {/* Header with actions */}
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

      <div ref={contentRef} className="space-y-6">
        {/* Summary */}
        {summary && (
          <Card>
            <p className="text-gray-700 leading-relaxed">{summary}</p>
            {detailed_analysis && (
              <>
                <button
                  onClick={() => setSummaryExpanded(!summaryExpanded)}
                  className="mt-2 text-sm text-violet-600 hover:text-violet-700 font-medium flex items-center gap-1"
                >
                  {summaryExpanded ? 'Daha az goster' : 'Detayli analizi goster'}
                  <ChevronDown className={`w-3 h-3 transition-transform duration-200 ${summaryExpanded ? 'rotate-180' : ''}`} />
                </button>
                <div
                  className="overflow-hidden transition-all duration-300 ease-in-out"
                  style={{ maxHeight: summaryExpanded ? '1000px' : '0px' }}
                >
                  <p className="text-gray-600 leading-relaxed mt-3 pt-3 border-t border-gray-100">
                    {detailed_analysis}
                  </p>
                </div>
              </>
            )}
          </Card>
        )}

        {/* Key Insights */}
        {key_insights.length > 0 && (
          <Card title="Onemli Bulgular">
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

        {/* Recommendations — accordion */}
        {recommendations.length > 0 && (
          <div className="space-y-3">
            <h4 className="text-base font-semibold text-gray-900 flex items-center gap-2">
              <TrendingUp className="w-4 h-4" />
              Iyilestirme Onerileri
            </h4>
            {recommendations.map((rec, i) => (
              <RecommendationCard
                key={i}
                rec={rec}
                index={i}
                defaultOpen={i === 0}
              />
            ))}
          </div>
        )}

        {/* Not Recommended — collapsible */}
        {not_recommended.length > 0 && (
          <CollapsibleSection
            title="Onerilmeyen Cozumler"
            icon={XCircle}
            iconColor="text-gray-400"
            defaultOpen={false}
          >
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
          </CollapsibleSection>
        )}

        {/* Action Plan — collapsible */}
        {hasActionPlan && (
          <CollapsibleSection
            title="Aksiyon Plani"
            icon={null}
            defaultOpen={false}
          >
            <ActionTimeline actionPlan={action_plan} />
          </CollapsibleSection>
        )}

        {/* Warnings */}
        {warnings.length > 0 && (
          <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <AlertTriangle className="w-4 h-4 text-amber-600" />
              <span className="text-sm font-medium text-amber-800">Uyarilar</span>
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

export default AITab;
