import { useState } from 'react';
import { Thermometer, Layers, Activity, Play } from 'lucide-react';
import Card from '../common/Card';
import PinchTab from '../pinch/PinchTab';
import AdvancedExergyTab from '../advanced-exergy/AdvancedExergyTab';
import EntropyGenerationTab from '../entropy-generation/EntropyGenerationTab';

const SUB_TABS = [
  { id: 'pinch', label: 'Pinch', icon: Thermometer },
  { id: 'advanced', label: 'İleri Exergy', icon: Layers },
  { id: 'egm', label: 'Entropi Üretimi', icon: Activity },
];

const EmptySubState = ({ label, onRun, isLoading }) => (
  <div className="flex flex-col items-center justify-center py-16 text-center">
    <div className="w-12 h-12 rounded-full bg-slate-100 flex items-center justify-center mb-4">
      <Play className="w-5 h-5 text-slate-400" />
    </div>
    <p className="text-slate-500 mb-4">{label} analizi henüz çalıştırılmadı.</p>
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

const DeepAnalysisTab = ({
  analysisResult,
  pinchLoading,
  advExergyLoading,
  egmLoading,
  onPinchRerun,
  onAdvancedExergyRerun,
  onEGMRerun,
}) => {
  const [activeSubTab, setActiveSubTab] = useState('pinch');

  const subTabHasData = {
    pinch: !!analysisResult?.pinch_analysis,
    advanced: !!analysisResult?.advanced_exergy,
    egm: !!analysisResult?.entropy_generation,
  };

  const renderSubContent = () => {
    switch (activeSubTab) {
      case 'pinch':
        return analysisResult?.pinch_analysis ? (
          <PinchTab
            pinchData={analysisResult.pinch_analysis}
            onRerun={onPinchRerun}
            isLoading={pinchLoading}
          />
        ) : (
          <Card>
            <EmptySubState
              label="Pinch"
              onRun={() => onPinchRerun?.({ delta_T_min_C: 10 })}
              isLoading={pinchLoading}
            />
          </Card>
        );

      case 'advanced':
        return analysisResult?.advanced_exergy ? (
          <AdvancedExergyTab
            advancedExergyData={analysisResult.advanced_exergy}
            onRerun={onAdvancedExergyRerun}
            isLoading={advExergyLoading}
          />
        ) : (
          <Card>
            <EmptySubState
              label="İleri Exergy"
              onRun={onAdvancedExergyRerun}
              isLoading={advExergyLoading}
            />
          </Card>
        );

      case 'egm':
        return analysisResult?.entropy_generation ? (
          <EntropyGenerationTab
            entropyData={analysisResult.entropy_generation}
            onRerun={onEGMRerun}
            isLoading={egmLoading}
          />
        ) : (
          <Card>
            <EmptySubState
              label="EGM"
              onRun={onEGMRerun}
              isLoading={egmLoading}
            />
          </Card>
        );

      default:
        return null;
    }
  };

  return (
    <div className="space-y-4">
      {/* Sub-tab navigation */}
      <div className="flex items-center gap-1 bg-slate-100 p-1 rounded-lg w-fit">
        {SUB_TABS.map((tab) => {
          const Icon = tab.icon;
          const isActive = activeSubTab === tab.id;
          const hasData = subTabHasData[tab.id];

          return (
            <button
              key={tab.id}
              onClick={() => setActiveSubTab(tab.id)}
              className={`flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded-md transition-colors ${
                isActive
                  ? 'bg-white text-cyan-700 shadow-sm'
                  : 'text-slate-500 hover:text-slate-700'
              }`}
            >
              <Icon className="w-4 h-4" />
              {tab.label}
              {hasData && (
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 flex-shrink-0" />
              )}
            </button>
          );
        })}
      </div>

      {/* Sub-tab content */}
      <div key={activeSubTab} className="animate-fade-in">
        {renderSubContent()}
      </div>
    </div>
  );
};

export default DeepAnalysisTab;
