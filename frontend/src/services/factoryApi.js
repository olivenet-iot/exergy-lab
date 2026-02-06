import api from './api';

export const createFactoryProject = async (name, sector, description) => {
  const response = await api.post('/factory/projects', { name, sector, description });
  return response.data;
};

export const getFactoryProjects = async () => {
  const response = await api.get('/factory/projects');
  return response.data;
};

export const getFactoryProject = async (projectId) => {
  const response = await api.get(`/factory/projects/${projectId}`);
  return response.data;
};

export const addEquipmentToProject = async (projectId, equipment) => {
  const response = await api.post(`/factory/projects/${projectId}/equipment`, equipment);
  return response.data;
};

export const removeEquipmentFromProject = async (projectId, equipmentId) => {
  const response = await api.delete(`/factory/projects/${projectId}/equipment/${equipmentId}`);
  return response.data;
};

export const analyzeFactory = async (projectId) => {
  const response = await api.post(`/factory/projects/${projectId}/analyze`);
  return response.data;
};

export const interpretFactory = async (projectId, sector) => {
  const response = await api.post(`/factory/projects/${projectId}/interpret`, { sector });
  return response.data;
};

export const runPinchAnalysis = async (projectId, params = {}) => {
  const response = await api.post(`/factory/projects/${projectId}/pinch`, params);
  return response.data;
};

export const runAdvancedExergy = async (projectId) => {
  const response = await api.post(`/factory/projects/${projectId}/advanced-exergy`);
  return response.data;
};

export const runEntropyGeneration = async (projectId) => {
  const response = await api.post(`/factory/projects/${projectId}/entropy-generation`);
  return response.data;
};
