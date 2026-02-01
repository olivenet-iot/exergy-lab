import { useState } from 'react';
import { analyzeCompressor, analyzeEquipment, getSolutions, interpretAnalysis } from '../services/api';

export const useAnalysis = () => {
  const [result, setResult] = useState(null);
  const [solutions, setSolutions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [interpretation, setInterpretation] = useState(null);
  const [aiLoading, setAiLoading] = useState(false);

  const analyze = async (equipmentType, subtype, parameters) => {
    setLoading(true);
    setError(null);
    setInterpretation(null);

    try {
      let analysisResult;

      if (equipmentType === 'compressor') {
        // Use legacy compressor endpoint for backward compatibility
        analysisResult = await analyzeCompressor(subtype, parameters);
      } else {
        // Use generic equipment endpoint
        analysisResult = await analyzeEquipment(equipmentType, subtype, parameters);
      }

      setResult(analysisResult ?? null);

      // Solutions: only for compressors currently
      if (equipmentType === 'compressor') {
        try {
          const solutionsResult = await getSolutions(subtype, {
            efficiency: analysisResult?.metrics?.exergy_efficiency_percent,
            specific_power: (parameters?.power_kW ?? 0) / (parameters?.flow_rate_m3_min || 1),
            operating_hours: parameters?.operating_hours || 4000,
          });
          setSolutions(solutionsResult?.recommendations ?? []);
        } catch {
          setSolutions([]);
        }
      } else {
        setSolutions([]);
      }

      // Phase 1 complete: main results are ready
      setLoading(false);

      // Phase 2: AI interpretation (non-blocking, compressor only for now)
      if (equipmentType === 'compressor') {
        setAiLoading(true);
        try {
          const aiResult = await interpretAnalysis(analysisResult, subtype, parameters);
          if (aiResult?.success && aiResult?.interpretation?.ai_available) {
            setInterpretation(aiResult.interpretation);
          }
        } catch {
          // AI failure is silent
        } finally {
          setAiLoading(false);
        }
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
