import { GitBranch, RefreshCw, AlertTriangle } from 'lucide-react';
import Card from '../common/Card';
import AdvancedExergyMetricBar from './AdvancedExergyMetricBar';
import QuadrantChart from './QuadrantChart';
import AdvancedExergyPriorityList from './AdvancedExergyPriorityList';
import InteractionNetwork from './InteractionNetwork';

const AdvancedExergyTab = ({ advancedExergyData, onRerun, isLoading }) => {
  if (!advancedExergyData?.is_valid) {
    const msg = advancedExergyData?.error || 'Ileri exergy analizi icin yeterli ekipman yok';
    return (
      <Card title="Ileri Exergy Analizi (EN/EX)">
        <div className="text-center py-8">
          <GitBranch className="w-10 h-10 text-gray-300 mx-auto mb-3" />
          <p className="text-gray-500 text-sm">{msg}</p>
        </div>
      </Card>
    );
  }

  return (
    <div className="space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-semibold text-gray-800 flex items-center gap-2">
          <GitBranch className="w-5 h-5 text-emerald-600" />
          Ileri Exergy Analizi (EN/EX Dekompozisyon)
        </h3>
        {onRerun && (
          <button
            onClick={onRerun}
            disabled={isLoading}
            className="flex items-center gap-1 px-3 py-1 text-sm bg-emerald-600 text-white rounded hover:bg-emerald-700 transition-colors disabled:opacity-50"
          >
            {isLoading ? (
              <div className="animate-spin rounded-full h-3 w-3 border-b-2 border-white" />
            ) : (
              <RefreshCw className="w-3 h-3" />
            )}
            Yeniden Calistir
          </button>
        )}
      </div>

      {/* Metric Bar */}
      <AdvancedExergyMetricBar data={advancedExergyData} />

      {/* Quadrant Chart */}
      <Card title="4-Kadran Dekompozisyon">
        <QuadrantChart chartData={advancedExergyData.quadrant_chart_data} />
      </Card>

      {/* Priority + Interaction grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
        <div className="lg:col-span-2">
          <Card title="Iyilestirme Onceligi (AV-EN Sirali)">
            <AdvancedExergyPriorityList ranking={advancedExergyData.priority_ranking} />
          </Card>
        </div>
        <div>
          <Card title="Ekipman Etkilesimleri">
            <InteractionNetwork edges={advancedExergyData.interaction_network} />
          </Card>
        </div>
      </div>

      {/* Warnings */}
      {advancedExergyData.warnings?.length > 0 && (
        <div className="bg-amber-50 border border-amber-200 rounded-lg p-3">
          <div className="flex items-center gap-2 mb-1">
            <AlertTriangle className="w-4 h-4 text-amber-600" />
            <span className="text-sm font-medium text-amber-800">Uyarilar</span>
          </div>
          <ul className="text-xs text-amber-700 space-y-1">
            {advancedExergyData.warnings.map((w, i) => (
              <li key={i}>{w}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default AdvancedExergyTab;
