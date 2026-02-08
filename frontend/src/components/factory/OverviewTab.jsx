import { Package } from 'lucide-react';
import Card from '../common/Card';
import FactoryAIPanel from './FactoryAIPanel';
import PriorityList from './PriorityList';
import IntegrationPanel from './IntegrationPanel';

const OverviewTab = ({
  interpretation,
  interpreting,
  onRequestAI,
  hasAnalysis,
  analysisResult,
  projectId,
  sector,
  onEquipmentClick,
  onSwitchTab,
}) => {
  const aggregates = analysisResult?.aggregates;
  const equipmentCount = analysisResult?.equipment_results?.length || 0;

  return (
    <div className="space-y-6">
      {/* AI Interpretation Panel */}
      <FactoryAIPanel
        interpretation={interpretation}
        loading={interpreting}
        onRequestAI={onRequestAI}
        hasAnalysis={hasAnalysis}
        analysisResult={analysisResult}
        projectId={projectId}
        sector={sector}
      />

      {/* Priorities + Integration side by side */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <Card title="İyileştirme Öncelik Listesi">
            <PriorityList
              hotspots={analysisResult?.hotspots}
              equipmentResults={analysisResult?.equipment_results}
              totalDestroyed={aggregates?.total_exergy_destroyed_kW}
              onEquipmentClick={onEquipmentClick}
            />
          </Card>
        </div>
        <div className="space-y-6">
          <Card title="Entegrasyon Fırsatları">
            <IntegrationPanel
              opportunities={analysisResult?.integration_opportunities}
            />
          </Card>

          {/* Equipment count summary */}
          {equipmentCount > 0 && (
            <Card>
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <Package className="w-4 h-4 text-gray-400" />
                  <span className="text-sm text-gray-600">{equipmentCount} ekipman analiz edildi</span>
                </div>
                <button
                  onClick={() => onSwitchTab?.('management')}
                  className="text-sm text-cyan-600 hover:text-cyan-700 font-medium"
                >
                  Envantere Git
                </button>
              </div>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
};

export default OverviewTab;
