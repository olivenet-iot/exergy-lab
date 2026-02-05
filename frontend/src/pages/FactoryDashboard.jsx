import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Factory, Plus, Play, PackageOpen } from 'lucide-react';
import {
  getFactoryProject,
  analyzeFactory,
  interpretFactory,
  addEquipmentToProject,
  removeEquipmentFromProject,
  runPinchAnalysis,
} from '../services/factoryApi';
import Card from '../components/common/Card';
import EquipmentInventory from '../components/factory/EquipmentInventory';
import AddEquipmentModal from '../components/factory/AddEquipmentModal';
import FactoryHeader from '../components/factory/FactoryHeader';
import FactoryMetricBar from '../components/factory/FactoryMetricBar';
import PriorityList from '../components/factory/PriorityList';
import IntegrationPanel from '../components/factory/IntegrationPanel';
import FactorySankey from '../components/factory/FactorySankey';
import FactoryAIPanel from '../components/factory/FactoryAIPanel';
import PinchTab from '../components/pinch/PinchTab';

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
  const [pinchLoading, setPinchLoading] = useState(false);

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

  const handleEquipmentClick = (hotspot) => {
    navigate(`/equipment/${hotspot.equipment_type}`, {
      state: { equipmentId: hotspot.id, fromFactory: projectId },
    });
  };

  const handlePinchRerun = async (params) => {
    setPinchLoading(true);
    try {
      const data = await runPinchAnalysis(projectId, params);
      setAnalysisResult((prev) => ({
        ...prev,
        pinch_analysis: data.pinch_analysis,
      }));
    } catch {
      // Keep existing pinch data on error
    } finally {
      setPinchLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center py-24">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-cyan-600" />
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
  const hasEquipment = (project.equipment?.length || 0) > 0;
  const hasAnalysis = !!analysisResult;
  const integrationPotential = analysisResult?.integration_opportunities?.reduce(
    (sum, opp) => sum + (opp.estimated_savings_EUR_year || 0),
    0
  ) || null;

  return (
    <div className="space-y-6">
      {/* Header - always visible */}
      <FactoryHeader
        project={project}
        onRefreshAnalysis={handleAnalyze}
        onAddEquipment={() => setShowModal(true)}
        isAnalyzing={analyzing}
      />

      {/* Error */}
      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700">
          {error}
        </div>
      )}

      {/* Mode 1: Empty - no equipment */}
      {!hasEquipment && (
        <Card>
          <div className="text-center py-12">
            <PackageOpen className="w-12 h-12 text-gray-300 mx-auto mb-4" />
            <h3 className="text-lg font-semibold text-gray-700 mb-2">
              Henuz ekipman eklenmedi
            </h3>
            <p className="text-gray-500 mb-4">
              Fabrika analizine baslamak icin ekipman ekleyin
            </p>
            <button
              onClick={() => setShowModal(true)}
              className="flex items-center gap-2 px-4 py-2 mx-auto bg-cyan-600 text-white rounded-lg hover:bg-cyan-700 transition-colors"
            >
              <Plus className="w-4 h-4" />
              Ekipman Ekle
            </button>
          </div>
        </Card>
      )}

      {/* Mode 2: Has equipment, no analysis */}
      {hasEquipment && !hasAnalysis && (
        <>
          <Card>
            <div className="text-center py-8">
              <Factory className="w-10 h-10 text-gray-300 mx-auto mb-3" />
              <h3 className="text-lg font-semibold text-gray-700 mb-2">
                Analiz hazir
              </h3>
              <p className="text-gray-500 mb-4">
                {project.equipment?.length} ekipman eklendi. Fabrika exergy analizini baslatabilirsiniz.
              </p>
              <button
                onClick={handleAnalyze}
                disabled={analyzing}
                className="flex items-center gap-2 px-4 py-2 mx-auto bg-cyan-600 text-white rounded-lg hover:bg-cyan-700 transition-colors disabled:opacity-50"
              >
                {analyzing ? (
                  <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white" />
                ) : (
                  <Play className="w-4 h-4" />
                )}
                Analiz Calistir
              </button>
            </div>
          </Card>

          <Card title="Ekipman Envanteri">
            <EquipmentInventory
              equipment={project.equipment || []}
              onRemove={handleRemoveEquipment}
            />
          </Card>
        </>
      )}

      {/* Mode 3: Full dashboard */}
      {hasEquipment && hasAnalysis && (
        <>
          {/* Metric Bar */}
          <FactoryMetricBar
            aggregates={aggregates}
            integrationPotential={integrationPotential}
          />

          {/* Priority List + Integration Panel grid */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2">
              <Card title="Iyilestirme Oncelik Listesi">
                <PriorityList
                  hotspots={analysisResult?.hotspots}
                  equipmentResults={analysisResult?.equipment_results}
                  totalDestroyed={aggregates?.total_exergy_destroyed_kW}
                  onEquipmentClick={handleEquipmentClick}
                />
              </Card>
            </div>
            <div>
              <Card title="Entegrasyon Firsatlari">
                <IntegrationPanel
                  opportunities={analysisResult?.integration_opportunities}
                />
              </Card>
            </div>
          </div>

          {/* Sankey Diagram */}
          {analysisResult?.sankey && (
            <Card title="Fabrika Exergy Akis Diyagrami">
              <FactorySankey data={analysisResult.sankey} />
            </Card>
          )}

          {/* Pinch Analysis */}
          {analysisResult?.pinch_analysis && (
            <PinchTab
              pinchData={analysisResult.pinch_analysis}
              onRerun={handlePinchRerun}
              isLoading={pinchLoading}
            />
          )}

          {/* AI Panel */}
          <FactoryAIPanel
            interpretation={interpretation}
            loading={interpreting}
            onRequestAI={handleInterpret}
            hasAnalysis={hasAnalysis}
          />

          {/* Equipment Inventory */}
          <Card title="Ekipman Envanteri">
            <EquipmentInventory
              equipment={project.equipment || []}
              onRemove={handleRemoveEquipment}
            />
          </Card>
        </>
      )}

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
