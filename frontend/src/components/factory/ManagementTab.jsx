import { Play } from 'lucide-react';
import Card from '../common/Card';
import EnergyManagementTab from '../energy-management/EnergyManagementTab';
import EquipmentInventory from './EquipmentInventory';

const EmptyEMState = ({ onRun, isLoading }) => (
  <div className="flex flex-col items-center justify-center py-16 text-center">
    <div className="w-12 h-12 rounded-full bg-slate-100 flex items-center justify-center mb-4">
      <Play className="w-5 h-5 text-slate-400" />
    </div>
    <p className="text-slate-500 mb-4">Enerji yönetimi analizi henüz çalıştırılmadı.</p>
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

const ManagementTab = ({
  analysisResult,
  emLoading,
  onEMRerun,
  equipment,
  onRemoveEquipment,
}) => {
  const hasEMData = !!analysisResult?.energy_management;

  return (
    <div className="space-y-6">
      {/* Energy Management (ISO 50001) */}
      {hasEMData ? (
        <EnergyManagementTab
          emData={analysisResult.energy_management}
          onRerun={onEMRerun}
          isLoading={emLoading}
        />
      ) : (
        <Card title="Enerji Yönetimi">
          <EmptyEMState onRun={onEMRerun} isLoading={emLoading} />
        </Card>
      )}

      {/* Equipment Inventory */}
      <Card title="Ekipman Envanteri">
        <EquipmentInventory
          equipment={equipment || []}
          onRemove={onRemoveEquipment}
        />
      </Card>
    </div>
  );
};

export default ManagementTab;
