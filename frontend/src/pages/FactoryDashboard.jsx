import { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Factory, Plus, Play, PackageOpen, ChevronDown, ChevronRight } from 'lucide-react';
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
import EquipmentInventory from '../components/factory/EquipmentInventory';
import AddEquipmentModal from '../components/factory/AddEquipmentModal';
import FactoryHeader from '../components/factory/FactoryHeader';
import FactoryMetricBar from '../components/factory/FactoryMetricBar';
import PriorityList from '../components/factory/PriorityList';
import IntegrationPanel from '../components/factory/IntegrationPanel';
import FactorySankey from '../components/factory/FactorySankey';
import FactoryAIPanel from '../components/factory/FactoryAIPanel';
import PinchTab from '../components/pinch/PinchTab';
import AdvancedExergyTab from '../components/advanced-exergy/AdvancedExergyTab';
import EntropyGenerationTab from '../components/entropy-generation/EntropyGenerationTab';
import ThermoeconomicTab from '../components/thermoeconomic/ThermoeconomicTab';
import EnergyManagementTab from '../components/energy-management/EnergyManagementTab';

/* ---------- Section nav items ---------- */
const SECTION_IDS = {
  ai: 'section-ai',
  priority: 'section-priority',
  sankey: 'section-sankey',
  pinch: 'section-pinch',
  advExergy: 'section-adv-exergy',
  egm: 'section-egm',
  thermoOpt: 'section-thermo-opt',
  energyMgmt: 'section-energy-mgmt',
  inventory: 'section-inventory',
};

/* ---------- Collapsible Section Wrapper ---------- */
const CollapsibleSection = ({ id, title, icon: Icon, iconColor, defaultOpen = false, children }) => {
  const [open, setOpen] = useState(defaultOpen);

  return (
    <div id={id} className="scroll-mt-20">
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center gap-2 w-full text-left mb-3 group"
      >
        {open ? (
          <ChevronDown className="w-4 h-4 text-gray-400 group-hover:text-gray-600 transition-colors" />
        ) : (
          <ChevronRight className="w-4 h-4 text-gray-400 group-hover:text-gray-600 transition-colors" />
        )}
        {Icon && <Icon className={`w-5 h-5 ${iconColor || 'text-gray-600'}`} />}
        <span className="text-lg font-semibold text-gray-800">{title}</span>
      </button>
      {open && <div className="transition-all duration-200">{children}</div>}
    </div>
  );
};

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
  const [advExergyLoading, setAdvExergyLoading] = useState(false);
  const [egmLoading, setEgmLoading] = useState(false);
  const [thermoOptLoading, setThermoOptLoading] = useState(false);
  const [emLoading, setEmLoading] = useState(false);
  const [activeSection, setActiveSection] = useState(null);

  const sectionRefs = useRef({});

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

  // Intersection observer for active section highlighting
  useEffect(() => {
    if (!analysisResult) return;

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            setActiveSection(entry.target.id);
          }
        }
      },
      { rootMargin: '-100px 0px -60% 0px', threshold: 0.1 }
    );

    // Observe all section elements
    Object.values(SECTION_IDS).forEach((id) => {
      const el = document.getElementById(id);
      if (el) observer.observe(el);
    });

    return () => observer.disconnect();
  }, [analysisResult]);

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

      // Auto-trigger AI interpretation after analysis completes
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
      // Clear analysis results since equipment changed
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

  const scrollToSection = (sectionId) => {
    const el = document.getElementById(sectionId);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
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

  // Build visible section nav items
  const navItems = [];
  if (hasAnalysis) {
    navItems.push({ id: SECTION_IDS.ai, label: 'AI Yorum' });
    navItems.push({ id: SECTION_IDS.priority, label: 'Öncelikler' });
    if (analysisResult?.sankey) navItems.push({ id: SECTION_IDS.sankey, label: 'Sankey' });
    if (analysisResult?.pinch_analysis) navItems.push({ id: SECTION_IDS.pinch, label: 'Pinch' });
    if (analysisResult?.advanced_exergy) navItems.push({ id: SECTION_IDS.advExergy, label: 'İleri Exergy' });
    if (analysisResult?.entropy_generation) navItems.push({ id: SECTION_IDS.egm, label: 'EGM' });
    if (analysisResult?.thermoeconomic_optimization) navItems.push({ id: SECTION_IDS.thermoOpt, label: 'Termoekonomik' });
    if (analysisResult?.energy_management) navItems.push({ id: SECTION_IDS.energyMgmt, label: 'Enerji Yönetimi' });
    navItems.push({ id: SECTION_IDS.inventory, label: 'Envanter' });
  }

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

      {/* Mode 3: Full dashboard */}
      {hasEquipment && hasAnalysis && (
        <>
          {/* Metric Bar */}
          <FactoryMetricBar
            aggregates={aggregates}
            integrationPotential={integrationPotential}
          />

          {/* Sticky Section Navigation */}
          {navItems.length > 0 && (
            <div className="sticky top-0 z-10 bg-white/95 backdrop-blur-sm border-b border-gray-200 -mx-6 px-6 py-2">
              <div className="flex items-center gap-1 overflow-x-auto">
                {navItems.map((item) => (
                  <button
                    key={item.id}
                    onClick={() => scrollToSection(item.id)}
                    className={`px-3 py-1.5 text-xs font-medium rounded-full whitespace-nowrap transition-colors ${
                      activeSection === item.id
                        ? 'bg-cyan-100 text-cyan-700'
                        : 'text-gray-500 hover:bg-gray-100 hover:text-gray-700'
                    }`}
                  >
                    {item.label}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* AI Panel — MOVED TO TOP (right after MetricBar) */}
          <div id={SECTION_IDS.ai} className="scroll-mt-20">
            <FactoryAIPanel
              interpretation={interpretation}
              loading={interpreting}
              onRequestAI={handleInterpret}
              hasAnalysis={hasAnalysis}
              analysisResult={analysisResult}
              projectId={projectId}
              sector={project?.sector}
            />
          </div>

          {/* Priority List + Integration Panel grid */}
          <div id={SECTION_IDS.priority} className="scroll-mt-20 grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2">
              <Card title="İyileştirme Öncelik Listesi">
                <PriorityList
                  hotspots={analysisResult?.hotspots}
                  equipmentResults={analysisResult?.equipment_results}
                  totalDestroyed={aggregates?.total_exergy_destroyed_kW}
                  onEquipmentClick={handleEquipmentClick}
                />
              </Card>
            </div>
            <div>
              <Card title="Entegrasyon Fırsatları">
                <IntegrationPanel
                  opportunities={analysisResult?.integration_opportunities}
                />
              </Card>
            </div>
          </div>

          {/* Sankey Diagram */}
          {analysisResult?.sankey && (
            <div id={SECTION_IDS.sankey} className="scroll-mt-20">
              <Card title="Fabrika Exergy Akış Diyagramı">
                <FactorySankey data={analysisResult.sankey} />
              </Card>
            </div>
          )}

          {/* Advanced Analysis Sections — Collapsible */}
          {analysisResult?.pinch_analysis && (
            <CollapsibleSection
              id={SECTION_IDS.pinch}
              title="Pinch Analizi"
              defaultOpen={false}
            >
              <PinchTab
                pinchData={analysisResult.pinch_analysis}
                onRerun={handlePinchRerun}
                isLoading={pinchLoading}
              />
            </CollapsibleSection>
          )}

          {analysisResult?.advanced_exergy && (
            <CollapsibleSection
              id={SECTION_IDS.advExergy}
              title="İleri Exergy Analizi (EN/EX)"
              defaultOpen={false}
            >
              <AdvancedExergyTab
                advancedExergyData={analysisResult.advanced_exergy}
                onRerun={handleAdvancedExergyRerun}
                isLoading={advExergyLoading}
              />
            </CollapsibleSection>
          )}

          {analysisResult?.entropy_generation && (
            <CollapsibleSection
              id={SECTION_IDS.egm}
              title="Entropi Üretimi Analizi (EGM)"
              defaultOpen={false}
            >
              <EntropyGenerationTab
                entropyData={analysisResult.entropy_generation}
                onRerun={handleEGMRerun}
                isLoading={egmLoading}
              />
            </CollapsibleSection>
          )}

          {analysisResult?.thermoeconomic_optimization && (
            <CollapsibleSection
              id={SECTION_IDS.thermoOpt}
              title="Termoekonomik Optimizasyon"
              defaultOpen={false}
            >
              <ThermoeconomicTab
                thermoData={analysisResult.thermoeconomic_optimization}
                onRerun={handleThermoOptRerun}
                isLoading={thermoOptLoading}
              />
            </CollapsibleSection>
          )}

          {analysisResult?.energy_management && (
            <CollapsibleSection
              id={SECTION_IDS.energyMgmt}
              title="Enerji Yönetimi (ISO 50001)"
              defaultOpen={false}
            >
              <EnergyManagementTab
                emData={analysisResult.energy_management}
                onRerun={handleEMRerun}
                isLoading={emLoading}
              />
            </CollapsibleSection>
          )}

          {/* Equipment Inventory */}
          <div id={SECTION_IDS.inventory} className="scroll-mt-20">
            <Card title="Ekipman Envanteri">
              <EquipmentInventory
                equipment={project.equipment || []}
                onRemove={handleRemoveEquipment}
              />
            </Card>
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
    </div>
  );
};

export default FactoryDashboard;
