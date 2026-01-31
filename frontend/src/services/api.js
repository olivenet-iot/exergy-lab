import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getCompressorTypes = async () => {
  const response = await api.get('/compressor-types');
  return response.data.types;
};

export const analyzeCompressor = async (compressorType, parameters) => {
  const response = await api.post('/analyze', {
    compressor_type: compressorType,
    parameters,
  });
  return response.data;
};

export const getBenchmarks = async (compressorType) => {
  const response = await api.get(`/benchmarks/${compressorType}`);
  return response.data;
};

export const getSolutions = async (compressorType, params) => {
  const response = await api.get(`/solutions/${compressorType}`, { params });
  return response.data;
};

export default api;
