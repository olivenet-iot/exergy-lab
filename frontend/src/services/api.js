import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getCompressorTypes = async () => {
  const response = await api.get('/compressor-types');
  return response.data.compressor_types.map(ct => ({
    ...ct,
    id: ct.type,
    fields: ct.fields.map(f => ({
      ...f,
      id: f.name,
    })),
  }));
};

export const analyzeCompressor = async (compressorType, parameters) => {
  const response = await api.post('/analyze', {
    compressor_type: compressorType,
    parameters,
  });
  const data = response.data;
  return {
    metrics: {
      exergy_input_kW: data.metrics.exergy_input_kW,
      exergy_output_kW: data.metrics.exergy_output_kW,
      exergy_destroyed_kW: data.metrics.exergy_destroyed_kW,
      exergy_efficiency_percent: data.metrics.exergy_efficiency_pct,
      annual_loss_kWh: data.heat_recovery.annual_loss_kWh,
      annual_cost_eur: data.heat_recovery.annual_loss_EUR,
    },
    heat_recovery: {
      potential_kW: data.heat_recovery.heat_recovery_potential_kW,
      annual_savings_eur: data.heat_recovery.heat_recovery_savings_eur_year,
    },
    benchmark: {
      rating: data.benchmark.benchmark_comparison,
      percentile: data.benchmark.benchmark_percentile,
      comparison_text: data.benchmark.comparison_text,
    },
    sankey: data.sankey,
  };
};

export const getBenchmarks = async (compressorType) => {
  const response = await api.get(`/benchmarks/${compressorType}`);
  return response.data;
};

export const getSolutions = async (compressorType, params) => {
  const response = await api.get(`/solutions/${compressorType}`, { params });
  const data = response.data;
  return {
    ...data,
    recommendations: data.recommendations?.map(r => ({
      id: r.type,
      title: r.title,
      description: r.description,
      priority: r.priority,
      savings_eur_year: r.savings_eur_year,
      estimated_investment_eur: r.investment_eur,
      estimated_roi_years: r.payback_years,
    })) ?? [],
  };
};

export const interpretAnalysis = async (analysisResult, compressorType, parameters) => {
  const response = await api.post('/interpret', {
    analysis_result: analysisResult,
    compressor_type: compressorType,
    parameters,
  });
  return response.data;
};

export default api;
