import { useState } from 'react';
import { analyzeCompressor, getSolutions } from '../services/api';

export const useAnalysis = () => {
  const [result, setResult] = useState(null);
  const [solutions, setSolutions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const analyze = async (compressorType, parameters) => {
    setLoading(true);
    setError(null);

    try {
      const analysisResult = await analyzeCompressor(compressorType, parameters);
      setResult(analysisResult.data);

      const solutionsResult = await getSolutions(compressorType, {
        efficiency: analysisResult.data.metrics.exergy_efficiency_percent,
        specific_power: parameters.power_kW / parameters.flow_rate_m3_min,
        operating_hours: parameters.operating_hours || 4000,
      });
      setSolutions(solutionsResult.recommendations);
    } catch (err) {
      setError(err.response?.data?.detail || err.message);
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setResult(null);
    setSolutions([]);
    setError(null);
  };

  return { result, solutions, loading, error, analyze, reset };
};
