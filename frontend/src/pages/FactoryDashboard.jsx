import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Factory, Plus, Play, PackageOpen, Target, GitBranch, BarChart3, Microscope, Lightbulb, ClipboardList } from 'lucide-react';
import {
  getFactoryProject,
  analyzeFactory,
  interpretFactory,
  addEquipmentToProject,
  removeEquipmentFromProject,
  runPinchAnalysis,
  runAdvancedExergy,
  runEntropyGeneration,
  runThermoeconomicOptimization,
  runEnergyManagement,
} from '../services/factoryApi';
import Card from '../components/common/Card';
import AddEquipmentModal from '../components/factory/AddEquipmentModal';
import ProcessEditModal from '../components/factory/ProcessEditModal';
import FactoryHeader from '../components/factory/FactoryHeader';
import FactoryMetricBar from '../components/factory/FactoryMetricBar';
import FactorySankeyV2 from '../components/factory/FactorySankeyV2';
import EquipmentInventory from '../components/factory/EquipmentInventory';
import GapAnalysisTab from '../components/factory/GapAnalysisTab';
import OverviewTab from '../components/factory/OverviewTab';
import DeepAnalysisTab from '../components/factory/DeepAnalysisTab';
import ActionPlanTab from '../components/factory/ActionPlanTab';
import ManagementTab from '../components/factory/ManagementTab';

/* ---------- Tab definitions (6 tabs) ---------- */
const TABS = [
  { id: 'process', label: 'Proses', icon: Target },
  { id: 'overview', label: 'Genel Bakış', icon: BarChart3 },
  { id: 'flow', label: 'Sankey', icon: GitBranch },
  { id: 'deep', label: 'Derin Analiz', icon: Microscope },
  { id: 'action', label: 'Aksiyon Planı', icon: Lightbulb },
  { id: 'management', label: 'Yönetim', icon: ClipboardList },
];

/* ---------- Empty state placeholder ---------- */
const EmptyTabState = ({ label }) => (
  <div className="flex flex-col items-center justify-center py-16 text-center">
    <div className="w-12 h-12 rounded-full bg-slate-100 flex items-center justify-center mb-4">
      <Play className="w-5 h-5 text-slate-400" />
    </div>
    <p className="text-slate-500 mb-4">{label || 'Bu analiz'} henüz çalıştırılmadı.</p>
  </div>
);

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
  const [showProcessModal, setShowProcessModal] = useState(false);
  const [pinchLoading, setPinchLoading] = useState(false);
  const [advExergyLoading, setAdvExergyLoading] = useState(false);
  const [egmLoading, setEgmLoading] = useState(false);
  const [thermoOptLoading, setThermoOptLoading] = useState(false);
  const [emLoading, setEmLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('overview');

  const fetchProject = async () => {
    try {
      const data = await getFactoryProject(projectId);
      setProject(data.project);
    } catch {
      setError('Proje bulunamadı');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProject();
  }, [projectId]);

  // Set default tab based on project state
  useEffect(() => {
    if (project?.process_type) {
      setActiveTab('process');
    }
  }, [project?.process_type]);

  const handleAnalyze = async () => {
    setAnalyzing(true);
    setError(null);
    setAnalysisResult(null);
    setInterpretation(null);

    try {
      const data = await analyzeFactory(projectId);
      setAnalysisResult(data);
      await fetchProject();
      triggerAIInterpretation();
    } catch (err) {
      setError(err?.response?.data?.detail || 'Analiz başarısız');
    } finally {
      setAnalyzing(false);
    }
  };

  const triggerAIInterpretation = async () => {
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

  const handleInterpret = async () => {
    await triggerAIInterpretation();
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
      setError(err?.response?.data?.detail || 'Ekipman eklenemedi!');
    }
  };

  const handleRemoveEquipment = async (equipmentId) => {
    try {
      await removeEquipmentFromProject(projectId, equipmentId);
      await fetchProject();
      setAnalysisResult(null);
      setInterpretation(null);
    } catch (err) {
      setError(err?.response?.data?.detail || 'Ekipman silinemedi!');
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

  const handleAdvancedExergyRerun = async () => {
    setAdvExergyLoading(true);
    try {
      const data = await runAdvancedExergy(projectId);
      setAnalysisResult((prev) => ({
        ...prev,
        advanced_exergy: data.advanced_exergy,
      }));
    } catch {
      // Keep existing data on error
    } finally {
      setAdvExergyLoading(false);
    }
  };

  const handleEGMRerun = async () => {
    setEgmLoading(true);
    try {
      const data = await runEntropyGeneration(projectId);
      setAnalysisResult((prev) => ({
        ...prev,
        entropy_generation: data.entropy_generation,
      }));
    } catch {
      // Keep existing data on error
    } finally {
      setEgmLoading(false);
    }
  };

  const handleThermoOptRerun = async () => {
    setThermoOptLoading(true);
    try {
      const data = await runThermoeconomicOptimization(projectId);
      setAnalysisResult((prev) => ({
        ...prev,
        thermoeconomic_optimization: data.thermoeconomic_optimization,
      }));
    } catch {
      // Keep existing data on error
    } finally {
      setThermoOptLoading(false);
    }
  };

  const handleEMRerun = async () => {
    setEmLoading(true);
    try {
      const data = await runEnergyManagement(projectId);
      setAnalysisResult((prev) => ({
        ...prev,
        energy_management: data.energy_management,
      }));
    } catch {
      // Keep existing data on error
    } finally {
      setEmLoading(false);
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
        <p className="text-gray-500">Proje bulunamadı</p>
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
  const gapAnalysis = analysisResult?.gap_analysis;

  // Tab status: determines dot color
  const tabHasData = {
    process: !!gapAnalysis,
    overview: !!interpretation || interpreting || !!analysisResult?.hotspots,
    flow: !!analysisResult?.sankey,
    deep: !!(analysisResult?.pinch_analysis || analysisResult?.advanced_exergy || analysisResult?.entropy_generation),
    action: !!analysisResult?.thermoeconomic_optimization,
    management: true,
  };

  // Process tab special 3-color logic
  const getProcessDotColor = () => {
    if (gapAnalysis) return 'bg-emerald-500';
    if (project.process_type) return 'bg-amber-400';
    return null; // no dot
  };

  // Render tab content
  const renderTabContent = () => {
    switch (activeTab) {
      case 'process':
        return (
          <GapAnalysisTab
            analysisResult={analysisResult}
            project={project}
            onAddProcess={() => setShowProcessModal(true)}
            onEditProcess={() => setShowProcessModal(true)}
          />
        );

      case 'overview':
        return (
          <OverviewTab
            interpretation={interpretation}
            interpreting={interpreting}
            onRequestAI={handleInterpret}
            hasAnalysis={hasAnalysis}
            analysisResult={analysisResult}
            projectId={projectId}
            sector={project?.sector}
            onEquipmentClick={handleEquipmentClick}
            onSwitchTab={setActiveTab}
          />
        );

      case 'flow':
        return analysisResult?.sankey ? (
          <Card title="Fabrika Exergy Akış Diyagramı">
            <FactorySankeyV2
              sankeyData={analysisResult.sankey}
              equipmentResults={analysisResult.equipment_results}
              aggregates={analysisResult.aggregates}
              hotspots={analysisResult.hotspots}
              integrationOpportunities={analysisResult.integration_opportunities}
              advancedExergy={analysisResult.advanced_exergy}
            />
          </Card>
        ) : (
          <Card><EmptyTabState label="Sankey" /></Card>
        );

      case 'deep':
        return (
          <DeepAnalysisTab
            analysisResult={analysisResult}
            pinchLoading={pinchLoading}
            advExergyLoading={advExergyLoading}
            egmLoading={egmLoading}
            onPinchRerun={handlePinchRerun}
            onAdvancedExergyRerun={handleAdvancedExergyRerun}
            onEGMRerun={handleEGMRerun}
          />
        );

      case 'action':
        return (
          <ActionPlanTab
            analysisResult={analysisResult}
            thermoOptLoading={thermoOptLoading}
            onThermoOptRerun={handleThermoOptRerun}
          />
        );

      case 'management':
        return (
          <ManagementTab
            analysisResult={analysisResult}
            emLoading={emLoading}
            onEMRerun={handleEMRerun}
            equipment={project.equipment}
            onRemoveEquipment={handleRemoveEquipment}
          />
        );

      default:
        return null;
    }
  };

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
              Henüz ekipman eklenmedi
            </h3>
            <p className="text-gray-500 mb-4">
              Fabrika analizine başlamak için ekipman ekleyin
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
                Analiz hazır
              </h3>
              <p className="text-gray-500 mb-4">
                {project.equipment?.length} ekipman eklendi. Fabrika exergy analizini başlatabilirsiniz.
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
                Analiz Çalıştır
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

      {/* Mode 3: Full dashboard with tabs */}
      {hasEquipment && hasAnalysis && (
        <>
          {/* Metric Bar */}
          <FactoryMetricBar
            aggregates={aggregates}
            integrationPotential={integrationPotential}
            gapAnalysis={gapAnalysis}
          />

          {/* Tab Bar */}
          <div className="sticky top-0 z-10 bg-white border-b border-slate-200 -mx-6 px-6">
            <div className="flex items-center gap-1 overflow-x-auto py-1 scrollbar-none">
              {TABS.map((tab) => {
                const Icon = tab.icon;
                const isActive = activeTab === tab.id;
                const hasData = tabHasData[tab.id];
                const isOverviewLoading = tab.id === 'overview' && interpreting;

                return (
                  <button
                    key={tab.id}
                    onClick={() => setActiveTab(tab.id)}
                    className={`flex items-center gap-1.5 px-3 py-2 text-sm font-medium rounded-lg whitespace-nowrap transition-colors ${
                      isActive
                        ? 'bg-cyan-50 text-cyan-700'
                        : 'text-slate-500 hover:bg-slate-50 hover:text-slate-700'
                    }`}
                  >
                    <Icon className="w-4 h-4" />
                    {tab.label}
                    {/* Status dot */}
                    {tab.id === 'process' ? (
                      (() => {
                        const dotColor = getProcessDotColor();
                        return dotColor ? (
                          <span className={`w-1.5 h-1.5 rounded-full flex-shrink-0 ${dotColor}`} />
                        ) : null;
                      })()
                    ) : tab.id === 'overview' ? (
                      (interpretation || interpreting) && (
                        <span className={`w-1.5 h-1.5 rounded-full flex-shrink-0 ${
                          isOverviewLoading ? 'bg-violet-400 animate-pulse' : 'bg-violet-500'
                        }`} />
                      )
                    ) : (
                      hasData && tab.id !== 'management' && (
                        <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 flex-shrink-0" />
                      )
                    )}
                  </button>
                );
              })}
            </div>
          </div>

          {/* Tab Content */}
          <div key={activeTab} className="animate-fade-in">
            {renderTabContent()}
          </div>
        </>
      )}

      {/* Add Equipment Modal */}
      {showModal && (
        <AddEquipmentModal
          onAdd={handleAddEquipment}
          onClose={() => setShowModal(false)}
        />
      )}

      {/* Process Edit Modal */}
      {showProcessModal && (
        <ProcessEditModal
          projectId={projectId}
          onClose={() => setShowProcessModal(false)}
          onSuccess={() => { setShowProcessModal(false); fetchProject(); }}
        />
      )}
    </div>
  );
};

export default FactoryDashboard;
