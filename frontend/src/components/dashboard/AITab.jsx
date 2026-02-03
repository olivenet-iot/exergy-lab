import AIInterpretation from '../results/AIInterpretation';
import ChatPanel from '../chat/ChatPanel';

const AITab = ({ interpretation, aiLoading, equipmentType, subtype, result }) => {
  return (
    <div className="space-y-6">
      <AIInterpretation interpretation={interpretation} loading={aiLoading} />

      <ChatPanel
        equipmentType={equipmentType}
        subtype={subtype}
        analysisData={result}
        isVisible={true}
        onClose={() => {}}
      />
    </div>
  );
};

export default AITab;
