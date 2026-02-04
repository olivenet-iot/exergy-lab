import { Sparkles } from 'lucide-react';
import Card from '../common/Card';
import FactoryAIInterpretation from './FactoryAIInterpretation';

const FactoryAIPanel = ({ interpretation, loading, onRequestAI, hasAnalysis }) => {
  return (
    <Card>
      <div className="flex items-center gap-2 mb-4">
        <Sparkles className="w-5 h-5 text-purple-500" />
        <h3 className="text-lg font-semibold text-gray-900">AI Fabrika Analizi</h3>
      </div>

      {!hasAnalysis && (
        <div className="text-center py-6">
          <p className="text-gray-400">Once fabrika analizini calistirin</p>
        </div>
      )}

      {hasAnalysis && !interpretation && !loading && (
        <div className="text-center py-6">
          <button
            onClick={onRequestAI}
            className="flex items-center gap-2 px-4 py-2 mx-auto bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors"
          >
            <Sparkles className="w-4 h-4" />
            AI Analizi Iste
          </button>
        </div>
      )}

      {hasAnalysis && loading && (
        <div className="flex items-center gap-3 py-8 justify-center">
          <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-purple-600" />
          <span className="text-gray-600">AI analizi hazirlaniyor...</span>
        </div>
      )}

      {hasAnalysis && interpretation && !loading && (
        <FactoryAIInterpretation interpretation={interpretation} loading={false} />
      )}
    </Card>
  );
};

export default FactoryAIPanel;
