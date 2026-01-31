import { useState } from 'react';
import { analyzeCompressor, getSolutions, interpretAnalysis } from '../services/api';

export const useAnalysis = () => {
  const [result, setResult] = useState(null);
  const [solutions, setSolutions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [interpretation, setInterpretation] = useState(null);
  const [aiLoading, setAiLoading] = useState(false);

  const analyze = async (compressorType, parameters) => {
    setLoading(true);
    setError(null);
    setInterpretation(null);

    try {
      const analysisResult = await analyzeCompressor(compressorType, parameters);
      setResult(analysisResult ?? null);

      const solutionsResult = await getSolutions(compressorType, {
        efficiency: analysisResult?.metrics?.exergy_efficiency_percent,
        specific_power: (parameters?.power_kW ?? 0) / (parameters?.flow_rate_m3_min || 1),
        operating_hours: parameters?.operating_hours || 4000,
      });
      setSolutions(solutionsResult?.recommendations ?? []);

      // Phase 1 complete: main results are ready
      setLoading(false);

      // Phase 2: AI interpretation (non-blocking)
      setAiLoading(true);
      try {
        const aiResult = await interpretAnalysis(analysisResult, compressorType, parameters);
        if (aiResult?.success && aiResult?.interpretation?.ai_available) {
          setInterpretation(aiResult.interpretation);
        }
      } catch {
        // AI failure is silent — does not affect main results
      } finally {
        setAiLoading(false);
      }
    } catch (err) {
      setError(err.response?.data?.detail || err.message);
      setLoading(false);
    }
  };

  const reset = () => {
    setResult(null);
    setSolutions([]);
    setError(null);
    setInterpretation(null);
  };

  return { result, solutions, loading, error, analyze, reset, interpretation, aiLoading };
};
