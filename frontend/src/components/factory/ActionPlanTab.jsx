import { Play } from 'lucide-react';
import Card from '../common/Card';
import ThermoeconomicTab from '../thermoeconomic/ThermoeconomicTab';
import IntegrationPanel from './IntegrationPanel';

const EmptyState = ({ onRun, isLoading }) => (
  <div className="flex flex-col items-center justify-center py-16 text-center">
    <div className="w-12 h-12 rounded-full bg-slate-100 flex items-center justify-center mb-4">
      <Play className="w-5 h-5 text-slate-400" />
    </div>
    <p className="text-slate-500 mb-4">Termoekonomik analiz henüz çalıştırılmadı.</p>
    {onRun && (
      <button
        onClick={onRun}
        disabled={isLoading}
        className="flex items-center gap-2 px-4 py-2 bg-cyan-600 text-white rounded-lg hover:bg-cyan-700 transition-colors disabled:opacity-50"
      >
        {isLoading ? (
          <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white" />
        ) : (
          <Play className="w-4 h-4" />
        )}
        Çalıştır
      </button>
    )}
  </div>
);

const ActionPlanTab = ({
  analysisResult,
  thermoOptLoading,
  onThermoOptRerun,
}) => {
  const hasThermoData = !!analysisResult?.thermoeconomic_optimization;
  const hasIntegration = analysisResult?.integration_opportunities?.length > 0;

  return (
    <div className="space-y-6">
      {/* Thermoeconomic Analysis */}
      {hasThermoData ? (
        <ThermoeconomicTab
          thermoData={analysisResult.thermoeconomic_optimization}
          onRerun={onThermoOptRerun}
          isLoading={thermoOptLoading}
        />
      ) : (
        <Card>
          <EmptyState onRun={onThermoOptRerun} isLoading={thermoOptLoading} />
        </Card>
      )}

      {/* Integration Opportunities */}
      {hasIntegration && (
        <Card title="Entegrasyon Fırsatları">
          <IntegrationPanel
            opportunities={analysisResult.integration_opportunities}
          />
        </Card>
      )}
    </div>
  );
};

export default ActionPlanTab;
