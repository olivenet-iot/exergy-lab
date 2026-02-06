import { useState, useRef, useEffect } from 'react';
import DOMPurify from 'dompurify';
import { chatWithAI } from '../../services/api';

/**
 * Simple regex-based markdown renderer.
 * Converts bold, italic, headers, code, lists, and line breaks to HTML.
 * Output is sanitized with DOMPurify to prevent XSS.
 */
function renderMarkdown(text) {
  if (!text) return '';
  let html = text
    // Code blocks (```...```)
    .replace(/```([\s\S]*?)```/g, '<pre class="bg-gray-100 rounded p-2 text-sm overflow-x-auto my-2"><code>$1</code></pre>')
    // Inline code (`...`)
    .replace(/`([^`]+)`/g, '<code class="bg-gray-100 px-1 rounded text-sm">$1</code>')
    // Bold (**...**)
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    // Italic (*...*)
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    // Headers (### ... , ## ... , # ...)
    .replace(/^### (.+)$/gm, '<h4 class="font-semibold text-sm mt-3 mb-1">$1</h4>')
    .replace(/^## (.+)$/gm, '<h3 class="font-semibold text-base mt-3 mb-1">$1</h3>')
    .replace(/^# (.+)$/gm, '<h2 class="font-bold text-lg mt-3 mb-1">$1</h2>')
    // Unordered lists (- ...)
    .replace(/^- (.+)$/gm, '<li class="ml-4 list-disc">$1</li>')
    // Ordered lists (1. ...)
    .replace(/^\d+\. (.+)$/gm, '<li class="ml-4 list-decimal">$1</li>')
    // Line breaks
    .replace(/\n/g, '<br/>');

  // Wrap consecutive <li> in <ul>
  html = html.replace(/((?:<li[^>]*>.*?<\/li><br\/>?)+)/g, (match) => {
    const cleaned = match.replace(/<br\/?>/g, '');
    return `<ul class="my-1">${cleaned}</ul>`;
  });

  return DOMPurify.sanitize(html);
}

const ChatPanel = ({ equipmentType, subtype, analysisData, isVisible, onClose }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const textareaRef = useRef(null);

  // Generate welcome message from analysisData
  useEffect(() => {
    if (isVisible && messages.length === 0 && analysisData) {
      const metrics = analysisData.metrics || {};
      const eff = metrics.exergy_efficiency_percent || metrics.exergy_efficiency_pct || 'N/A';
      const benchmark = analysisData.benchmark || {};
      const grade = analysisData.radar_data?.grade || analysisData.radar_data?.grade_letter || '';
      const rating = benchmark.rating || '';

      // Factory-specific welcome message
      const isFactory = equipmentType === 'factory';
      let welcomeText;

      if (isFactory) {
        const aggr = analysisData.aggregates || {};
        const factoryEff = aggr.factory_exergy_efficiency_pct;
        welcomeText = `Merhaba! Bu fabrika analiz sonuçlarınız hakkında sorularınızı yanıtlayabilirim.`;
        if (factoryEff != null) {
          welcomeText += `\n\nFabrika exergy veriminiz **%${typeof factoryEff === 'number' ? factoryEff.toFixed(1) : factoryEff}**.`;
        }
        welcomeText += '\n\nSize nasıl yardımcı olabilirim?';
      } else {
        welcomeText = `Merhaba! Bu ${equipmentType} analiz sonuçlarınız hakkında sorularınızı yanıtlayabilirim.`;
        if (eff !== 'N/A') {
          welcomeText += `\n\nMevcut exergy veriminiz **%${typeof eff === 'number' ? eff.toFixed(1) : eff}**`;
          if (rating) welcomeText += ` (${rating})`;
          if (grade) welcomeText += ` - Not: **${grade}**`;
          welcomeText += '.';
        }
        welcomeText += '\n\nSize nasıl yardımcı olabilirim?';
      }

      const suggestions = isFactory
        ? [
            'Fabrika exergy verimini nasıl artırabilirim?',
            'En büyük iyileştirme fırsatları neler?',
            'Ekipmanlar arası entegrasyon önerileri neler?',
          ]
        : [
            'Exergy verimini nasıl artırabilirim?',
            'Bu sonuçlar sektörel benchmark ile nasıl karşılaştırılır?',
            'Öncelikli iyileştirme önerileri neler?',
          ];

      setMessages([{
        role: 'assistant',
        content: welcomeText,
        knowledge_sources: [],
        follow_up_suggestions: suggestions,
      }]);
    }
  }, [isVisible, analysisData, equipmentType]);

  // Auto-scroll to bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  const sendMessage = async (text) => {
    const question = (text || input).trim();
    if (!question || isLoading) return;

    const userMsg = { role: 'user', content: question };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsLoading(true);

    try {
      // Build history from existing messages (user + assistant only)
      const history = messages
        .filter(m => m.role === 'user' || m.role === 'assistant')
        .map(m => ({ role: m.role, content: m.content }));

      const response = await chatWithAI({
        equipment_type: equipmentType,
        subtype: subtype || null,
        question,
        analysis_data: analysisData || null,
        history,
      });

      setMessages(prev => [...prev, {
        role: 'assistant',
        content: response.answer || 'Yanit alinamadi.',
        knowledge_sources: response.knowledge_sources || [],
        follow_up_suggestions: response.follow_up_suggestions || [],
      }]);
    } catch {
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: 'Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin.',
        knowledge_sources: [],
        follow_up_suggestions: [],
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const handleSuggestionClick = (suggestion) => {
    sendMessage(suggestion);
  };

  if (!isVisible) return null;

  return (
    <div className="bg-white border border-gray-200 rounded-xl overflow-hidden">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 bg-cyan-600 text-white">
        <div className="flex items-center gap-2">
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
          </svg>
          <span className="font-semibold text-sm">AI Danışmanı</span>
        </div>
        <button
          onClick={onClose}
          className="text-white/80 hover:text-white transition-colors"
          aria-label="Sohbeti kapat"
        >
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      {/* Messages — flexible height with min/max */}
      <div className="min-h-[16rem] max-h-[32rem] overflow-y-auto p-4 space-y-4 bg-gray-50">
        {messages.map((msg, idx) => (
          <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[85%] ${msg.role === 'user' ? 'order-last' : ''}`}>
              {/* Message bubble */}
              <div
                className={`rounded-lg px-4 py-2 text-sm ${
                  msg.role === 'user'
                    ? 'bg-cyan-600 text-white'
                    : 'bg-white border border-gray-200 text-gray-800'
                }`}
              >
                {msg.role === 'user' ? (
                  <p>{msg.content}</p>
                ) : (
                  <div
                    className="prose prose-sm max-w-none"
                    dangerouslySetInnerHTML={{ __html: renderMarkdown(msg.content) }}
                  />
                )}
              </div>

              {/* Knowledge sources badges */}
              {msg.knowledge_sources && msg.knowledge_sources.length > 0 && (
                <div className="flex flex-wrap gap-1 mt-1">
                  {msg.knowledge_sources.map((src, i) => (
                    <span
                      key={i}
                      className="text-[10px] bg-gray-200 text-gray-600 px-1.5 py-0.5 rounded"
                    >
                      {src}
                    </span>
                  ))}
                </div>
              )}

              {/* Follow-up suggestions */}
              {msg.follow_up_suggestions && msg.follow_up_suggestions.length > 0 && (
                <div className="flex flex-wrap gap-2 mt-2">
                  {msg.follow_up_suggestions.map((suggestion, i) => (
                    <button
                      key={i}
                      onClick={() => handleSuggestionClick(suggestion)}
                      disabled={isLoading}
                      className="text-xs bg-cyan-50 text-cyan-700 border border-cyan-200 px-2.5 py-1 rounded-full hover:bg-cyan-100 transition-colors disabled:opacity-50"
                    >
                      {suggestion}
                    </button>
                  ))}
                </div>
              )}
            </div>
          </div>
        ))}

        {/* Loading indicator */}
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-white border border-gray-200 rounded-lg px-4 py-2">
              <div className="flex space-x-1">
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input area */}
      <div className="border-t border-gray-200 p-3 bg-white">
        <div className="flex gap-2">
          <textarea
            ref={textareaRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Sorunuzu yazın..."
            rows={1}
            className="flex-1 resize-none border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
            disabled={isLoading}
          />
          <button
            onClick={() => sendMessage()}
            disabled={isLoading || !input.trim()}
            className="px-4 py-2 bg-cyan-600 text-white rounded-lg text-sm font-medium hover:bg-cyan-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatPanel;
