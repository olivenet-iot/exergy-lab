import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Factory, ArrowLeft, Play, Sparkles, Plus } from 'lucide-react';
import {
  getFactoryProject,
  analyzeFactory,
  interpretFactory,
  addEquipmentToProject,
  removeEquipmentFromProject,
} from '../services/factoryApi';
import Card from '../components/common/Card';
import { formatCurrency, formatNumber, formatPercentage } from '../utils/formatters';
import EquipmentInventory from '../components/factory/EquipmentInventory';
import AddEquipmentModal from '../components/factory/AddEquipmentModal';
import FactorySankey from '../components/factory/FactorySankey';
import HotspotList from '../components/factory/HotspotList';
import IntegrationOpportunities from '../components/factory/IntegrationOpportunities';
import FactoryAIInterpretation from '../components/factory/FactoryAIInterpretation';

const FactoryDashboard = () => {
  const { projectId } = useParams();
  const navigate = useNavigate();

  const [project, setProject] = useState(null);
  const [loading, setLoading] = useState(true);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [interpretation, setInterpretation] = useState(null);
  const [interpreting, setInterpreting] = useState(false);
  const [error, setError] = useState(null);
  const [showModal, setShowModal] = useState(false);

  const fetchProject = async () => {
    try {
      const data = await getFactoryProject(projectId);
      setProject(data.project);
    } catch {
      setError('Proje bulunamadi');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProject();
  }, [projectId]);

  const handleAnalyze = async () => {
    setAnalyzing(true);
    setError(null);
    setAnalysisResult(null);
    setInterpretation(null);

    try {
      const data = await analyzeFactory(projectId);
      setAnalysisResult(data);
      // Refresh project to get updated analysis results
      await fetchProject();
    } catch (err) {
      setError(err?.response?.data?.detail || 'Analiz basarisiz');
    } finally {
      setAnalyzing(false);
    }
  };

  const handleInterpret = async () => {
    setInterpreting(true);
    try {
      const data = await interpretFactory(projectId, project?.sector);
      setInterpretation(data.interpretation);
    } catch {
      setInterpretation({ ai_available: false });
    } finally {
      setInterpreting(false);
    }
  };

  const handleAddEquipment = async (eq) => {
    try {
      await addEquipmentToProject(projectId, {
        type: eq.type,
        subtype: eq.subtype,
        name: eq.name,
        parameters: eq.parameters,
      });
      setShowModal(false);
      await fetchProject();
    } catch (err) {
      setError(err?.response?.data?.detail || 'Ekipman eklenemedi');
    }
  };

  const handleRemoveEquipment = async (equipmentId) => {
    try {
      await removeEquipmentFromProject(projectId, equipmentId);
      await fetchProject();
      // Clear analysis results since equipment changed
      setAnalysisResult(null);
      setInterpretation(null);
    } catch (err) {
      setError(err?.response?.data?.detail || 'Ekipman silinemedi');
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center py-24">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600" />
      </div>
    );
  }

  if (!project) {
    return (
      <div className="text-center py-24">
        <p className="text-gray-500">Proje bulunamadi</p>
      </div>
    );
  }

  const aggregates = analysisResult?.aggregates;

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <button
            onClick={() => navigate('/factory')}
            className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <ArrowLeft className="w-5 h-5 text-gray-600" />
          </button>
          <Factory className="w-8 h-8 text-indigo-600" />
          <div>
            <h2 className="text-2xl font-bold text-gray-900">{project.name}</h2>
            <p className="text-gray-600 mt-1">
              {project.sector && <span className="capitalize">{project.sector}</span>}
              {project.sector && ' — '}
              {project.equipment_count} ekipman
            </p>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={handleAnalyze}
            disabled={analyzing || (project.equipment?.length || 0) === 0}
            className="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors disabled:opacity-50"
          >
            {analyzing ? (
              <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white" />
            ) : (
              <Play className="w-4 h-4" />
            )}
            Analiz Calistir
          </button>
          {analysisResult && (
            <button
              onClick={handleInterpret}
              disabled={interpreting}
              className="flex items-center gap-2 px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors disabled:opacity-50"
            >
              {interpreting ? (
                <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white" />
              ) : (
                <Sparkles className="w-4 h-4" />
              )}
              AI Yorumu
            </button>
          )}
        </div>
      </div>

      {/* Error */}
      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700">
          {error}
        </div>
      )}

      {/* Summary Metrics */}
      {aggregates && (
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <Card>
            <div className="text-sm text-gray-500">Toplam Guc</div>
            <div className="text-2xl font-bold text-gray-900 mt-1">
              {formatNumber(aggregates.total_exergy_input_kW, 1)} kW
            </div>
          </Card>
          <Card>
            <div className="text-sm text-gray-500">Exergy Kaybi</div>
            <div className="text-2xl font-bold text-red-600 mt-1">
              {formatNumber(aggregates.total_exergy_destroyed_kW, 1)} kW
            </div>
          </Card>
          <Card>
            <div className="text-sm text-gray-500">Fabrika Verimi</div>
            <div className="text-2xl font-bold text-indigo-600 mt-1">
              {formatPercentage(aggregates.factory_exergy_efficiency_pct)}
            </div>
          </Card>
          <Card>
            <div className="text-sm text-gray-500">Yillik Kayip</div>
            <div className="text-2xl font-bold text-amber-600 mt-1">
              {formatCurrency(aggregates.total_annual_loss_EUR)}
            </div>
          </Card>
        </div>
      )}

      {/* Equipment Inventory */}
      <Card title="Ekipman Envanteri">
        <EquipmentInventory
          equipment={project.equipment || []}
          onRemove={handleRemoveEquipment}
        />
        <div className="mt-4">
          <button
            onClick={() => setShowModal(true)}
            className="flex items-center gap-2 px-3 py-2 text-indigo-600 border border-indigo-300 rounded-lg hover:bg-indigo-50 transition-colors"
          >
            <Plus className="w-4 h-4" />
            Ekipman Ekle
          </button>
        </div>
      </Card>

      {/* Factory Sankey */}
      {analysisResult?.sankey && (
        <Card title="Fabrika Exergy Akis Diyagrami">
          <FactorySankey data={analysisResult.sankey} />
        </Card>
      )}

      {/* Hotspots */}
      {analysisResult?.hotspots?.length > 0 && (
        <Card title="Exergy Kayip Hotspot'lari">
          <HotspotList hotspots={analysisResult.hotspots} />
        </Card>
      )}

      {/* Integration Opportunities */}
      {analysisResult?.integration_opportunities?.length > 0 && (
        <IntegrationOpportunities opportunities={analysisResult.integration_opportunities} />
      )}

      {/* AI Interpretation */}
      <FactoryAIInterpretation interpretation={interpretation} loading={interpreting} />

      {/* Add Equipment Modal */}
      {showModal && (
        <AddEquipmentModal
          onAdd={handleAddEquipment}
          onClose={() => setShowModal(false)}
        />
      )}
    </div>
  );
};

export default FactoryDashboard;
