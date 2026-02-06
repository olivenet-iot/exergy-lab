import { Activity, RefreshCw, AlertTriangle } from 'lucide-react';
import Card from '../common/Card';
import EGMMetricBar from './EGMMetricBar';
import BejanNumberChart from './BejanNumberChart';
import EntropyDecompositionChart from './EntropyDecompositionChart';
import IrreversibilityRanking from './IrreversibilityRanking';

const EntropyGenerationTab = ({ entropyData, onRerun, isLoading }) => {
  if (!entropyData?.is_valid) {
    const msg = entropyData?.error_message || 'EGM analizi icin yeterli ekipman yok';
    return (
      <Card title="Entropi Uretimi Analizi (EGM)">
        <div className="text-center py-8">
          <Activity className="w-10 h-10 text-gray-300 mx-auto mb-3" />
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
          <Activity className="w-5 h-5 text-purple-600" />
          Entropi Uretimi Analizi (EGM)
        </h3>
        {onRerun && (
          <button
            onClick={onRerun}
            disabled={isLoading}
            className="flex items-center gap-1 px-3 py-1 text-sm bg-purple-600 text-white rounded hover:bg-purple-700 transition-colors disabled:opacity-50"
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
      <EGMMetricBar data={entropyData} />

      {/* Bejan Number Chart */}
      <Card title="Bejan Sayisi (N_s) - Tersinmezlik Haritasi">
        <BejanNumberChart chartData={entropyData.bejan_number_chart_data} />
      </Card>

      {/* Decomposition + Ranking grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
        <div className="lg:col-span-2">
          <Card title="Entropi Dekompozisyonu (DeltaT + DeltaP + Karisma)">
            <EntropyDecompositionChart chartData={entropyData.decomposition_chart_data} />
          </Card>
        </div>
        <div>
          <Card title="Tersinmezlik Siralamasi (N_s)">
            <IrreversibilityRanking ranking={entropyData.irreversibility_ranking} />
          </Card>
        </div>
      </div>

      {/* Warnings */}
      {entropyData.warnings?.length > 0 && (
        <div className="bg-amber-50 border border-amber-200 rounded-lg p-3">
          <div className="flex items-center gap-2 mb-1">
            <AlertTriangle className="w-4 h-4 text-amber-600" />
            <span className="text-sm font-medium text-amber-800">Uyarilar</span>
          </div>
          <ul className="text-xs text-amber-700 space-y-1">
            {entropyData.warnings.map((w, i) => (
              <li key={i}>{w}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default EntropyGenerationTab;
