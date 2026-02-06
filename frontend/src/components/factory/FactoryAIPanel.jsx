import { useState, useRef } from 'react';
import { Sparkles, RefreshCw, MessageCircle } from 'lucide-react';
import Card from '../common/Card';
import AIActionBar from '../common/AIActionBar';
import FactoryAIInterpretation from './FactoryAIInterpretation';
import ChatPanel from '../chat/ChatPanel';

const AI_TIMEOUT_SECONDS = 120;

const ProgressBar = ({ loading }) => {
  if (!loading) return null;

  return (
    <div className="space-y-3 py-6">
      <div className="flex items-center gap-3 justify-center">
        <Sparkles className="w-5 h-5 text-purple-500 animate-pulse" />
        <span className="text-gray-600">AI analizi hazırlanıyor...</span>
      </div>
      <div className="w-full max-w-md mx-auto">
        <div className="h-1.5 bg-gray-200 rounded-full overflow-hidden">
          <div
            className="h-full bg-purple-500 rounded-full"
            style={{
              animation: `progressBar ${AI_TIMEOUT_SECONDS}s linear forwards`,
            }}
          />
        </div>
        <p className="text-xs text-gray-400 text-center mt-1.5">
          AI yorumu genellikle 30-60 saniye sürer
        </p>
      </div>
      <style>{`
        @keyframes progressBar {
          0% { width: 0%; }
          15% { width: 30%; }
          50% { width: 60%; }
          80% { width: 85%; }
          100% { width: 95%; }
        }
      `}</style>
    </div>
  );
};

const FactoryAIPanel = ({
  interpretation,
  loading,
  onRequestAI,
  hasAnalysis,
  analysisResult,
  projectId,
  sector,
}) => {
  const [showChat, setShowChat] = useState(false);
  const contentRef = useRef(null);

  return (
    <Card>
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <Sparkles className="w-5 h-5 text-purple-500" />
          <h3 className="text-lg font-semibold text-gray-900">AI Fabrika Analizi</h3>
        </div>
        <div className="flex items-center gap-2">
          {/* Copy/PDF buttons — only when interpretation is ready */}
          {hasAnalysis && interpretation && !loading && interpretation.ai_available !== false && (
            <AIActionBar contentRef={contentRef} fileName="fabrika-ai-yorum" />
          )}
          {/* Chat toggle */}
          {hasAnalysis && (
            <button
              onClick={() => setShowChat(!showChat)}
              className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium rounded-lg transition-colors ${
                showChat
                  ? 'bg-cyan-100 text-cyan-700'
                  : 'text-gray-600 bg-gray-100 hover:bg-gray-200'
              }`}
            >
              <MessageCircle className="w-3.5 h-3.5" />
              Sohbet
            </button>
          )}
          {/* Rerun button */}
          {hasAnalysis && interpretation && !loading && (
            <button
              onClick={onRequestAI}
              className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-gray-600 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors"
              title="AI yorumunu yeniden çalıştır"
            >
              <RefreshCw className="w-3.5 h-3.5" />
              Yeniden
            </button>
          )}
        </div>
      </div>

      {!hasAnalysis && (
        <div className="text-center py-6">
          <p className="text-gray-400">Önce fabrika analizini çalıştırın</p>
        </div>
      )}

      {hasAnalysis && !interpretation && !loading && (
        <div className="text-center py-6">
          <button
            onClick={onRequestAI}
            className="flex items-center gap-2 px-4 py-2 mx-auto bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors"
          >
            <Sparkles className="w-4 h-4" />
            AI Analizi İste
          </button>
        </div>
      )}

      {hasAnalysis && loading && <ProgressBar loading={loading} />}

      {hasAnalysis && interpretation && !loading && (
        <div ref={contentRef}>
          <FactoryAIInterpretation interpretation={interpretation} loading={false} />
        </div>
      )}

      {/* Chat Panel for Factory */}
      {showChat && hasAnalysis && (
        <div className="mt-6 border-t border-gray-200 pt-4">
          <ChatPanel
            equipmentType="factory"
            subtype={sector || null}
            analysisData={analysisResult}
            isVisible={true}
            onClose={() => setShowChat(false)}
          />
        </div>
      )}
    </Card>
  );
};

export default FactoryAIPanel;
