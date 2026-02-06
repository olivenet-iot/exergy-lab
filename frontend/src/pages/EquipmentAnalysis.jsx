import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Wind, Flame, Snowflake, Droplets, ArrowLeftRight, Zap, Sun } from 'lucide-react';
import { getEquipmentConfig } from '../services/api';
import { useAnalysis } from '../hooks/useAnalysis';
import SubtypeSelector from '../components/equipment/SubtypeSelector';
import ParameterForm from '../components/forms/ParameterForm';
import Card from '../components/common/Card';
import LoadingSpinner from '../components/common/Loading';
import DashboardLayout from '../components/dashboard/DashboardLayout';
import ParameterSidebar from '../components/dashboard/ParameterSidebar';
import HeroScoreBanner from '../components/dashboard/HeroScoreBanner';
import TabContainer from '../components/dashboard/TabContainer';
import OverviewTab from '../components/dashboard/OverviewTab';
import FlowTab from '../components/dashboard/FlowTab';
import AITab from '../components/dashboard/AITab';
import ScenarioTab from '../components/dashboard/ScenarioTab';
import FloatingChat from '../components/chat/FloatingChat';

const EQUIPMENT_META = {
  compressor: { name: 'Kompresör', icon: Wind, color: 'text-blue-600' },
  boiler: { name: 'Kazan', icon: Flame, color: 'text-orange-600' },
  chiller: { name: 'Chiller', icon: Snowflake, color: 'text-cyan-600' },
  pump: { name: 'Pompa', icon: Droplets, color: 'text-emerald-600' },
  heat_exchanger: { name: 'Isı Eşanjörü', icon: ArrowLeftRight, color: 'text-purple-600' },
  steam_turbine: { name: 'Buhar Türbini', icon: Zap, color: 'text-yellow-600' },
  dryer: { name: 'Kurutma Fırını', icon: Sun, color: 'text-red-600' },
};

const TAB_CONFIG = [
  { id: 'overview', label: 'Genel Bakış' },
  { id: 'flow',     label: 'Akış Analizi' },
  { id: 'ai',       label: 'AI Danışman' },
  { id: 'scenario', label: 'Senaryo' },
];

const EquipmentAnalysis = () => {
  const { equipmentType } = useParams();
  const meta = EQUIPMENT_META[equipmentType] || { name: equipmentType, icon: Wind, color: 'text-gray-600' };
  const Icon = meta.icon;

  const [subtypes, setSubtypes] = useState([]);
  const [subtypesLoading, setSubtypesLoading] = useState(true);
  const [selectedSubtype, setSelectedSubtype] = useState(null);
  const [formValues, setFormValues] = useState({});
  const [baselineParams, setBaselineParams] = useState({});

  const { result, solutions, loading, error, analyze, reset, interpretation, aiLoading } = useAnalysis();

  // Dashboard state
  const [activeTab, setActiveTab] = useState('overview');
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

  // Fetch subtypes with field definitions when equipment type changes
  useEffect(() => {
    setSubtypes([]);
    setSelectedSubtype(null);
    setFormValues({});
    setActiveTab('overview');
    setSidebarCollapsed(false);
    reset();
    setSubtypesLoading(true);

    const fetchConfig = async () => {
      try {
        const data = await getEquipmentConfig(equipmentType);
        setSubtypes(data);
      } catch {
        setSubtypes([]);
      } finally {
        setSubtypesLoading(false);
      }
    };

    fetchConfig();
  }, [equipmentType]);

  const handleSubtypeSelect = (subtypeId) => {
    setSelectedSubtype(subtypeId);
    setFormValues({});
    setActiveTab('overview');
    reset();
  };

  const handleFormChange = (fieldId, value) => {
    setFormValues((prev) => ({ ...prev, [fieldId]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    analyze(equipmentType, selectedSubtype, formValues);
    setBaselineParams({ ...formValues });
  };

  const handleReanalyze = () => {
    analyze(equipmentType, selectedSubtype, formValues);
    setBaselineParams({ ...formValues });
  };

  const selectedSubtypeData = subtypes?.find((t) => (t.id || t.type) === selectedSubtype);

  // Build sidebar (only shown when result exists)
  const sidebar = result ? (
    <ParameterSidebar
      equipmentType={equipmentType}
      equipmentName={meta.name}
      equipmentIcon={Icon}
      equipmentColor={meta.color}
      subtype={selectedSubtypeData?.name || selectedSubtype}
      isCollapsed={sidebarCollapsed}
      onToggleCollapse={() => setSidebarCollapsed((prev) => !prev)}
      onReanalyze={handleReanalyze}
      loading={loading}
    >
      {selectedSubtypeData && (
        <ParameterForm
          fields={selectedSubtypeData.fields}
          values={formValues}
          onChange={handleFormChange}
          onSubmit={(e) => { e.preventDefault(); handleReanalyze(); }}
          loading={loading}
        />
      )}
    </ParameterSidebar>
  ) : null;

  // Build metric bar (only shown when result exists)
  const metricBar = result ? (
    <HeroScoreBanner
      efficiency={result.metrics?.exergy_efficiency_percent}
      grade={result.radar_data?.grade_letter}
      destructionKW={result.metrics?.exergy_destroyed_kW}
      avoidableKW={result.metrics?.exergy_destroyed_avoidable_kW}
      unavoidableKW={result.metrics?.exergy_destroyed_unavoidable_kW}
      annualLossEUR={result.metrics?.annual_cost_eur}
      avoidableRatio={result.metrics?.avoidable_ratio_pct}
    />
  ) : null;

  return (
    <DashboardLayout hasResult={!!result} sidebar={sidebar} metricBar={metricBar}>
      {!result ? (
        /* Pre-analysis: centered form */
        <div className="space-y-8">
          {/* Title */}
          <div className="flex items-center gap-3">
            <Icon className={`w-8 h-8 ${meta.color}`} />
            <div>
              <h2 className="text-2xl font-bold text-gray-900">{meta.name} Ekserji Analizi</h2>
              <p className="text-gray-600 mt-1">
                {meta.name} tipini seçin ve parametreleri girin
              </p>
            </div>
          </div>

          {/* Subtype Selection */}
          <Card title={`1. ${meta.name} Tipi`}>
            {subtypesLoading ? (
              <div className="h-32 flex items-center justify-center">
                <LoadingSpinner />
              </div>
            ) : (
              <SubtypeSelector
                subtypes={subtypes}
                selected={selectedSubtype}
                onSelect={handleSubtypeSelect}
              />
            )}
          </Card>

          {/* Parameter Form */}
          {selectedSubtypeData && (
            <>
              <Card title="2. Parametreler">
                <ParameterForm
                  fields={selectedSubtypeData.fields}
                  values={formValues}
                  onChange={handleFormChange}
                  onSubmit={handleSubmit}
                  loading={loading}
                />
              </Card>

              {error && (
                <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700">
                  {typeof error === 'string' ? error : JSON.stringify(error)}
                </div>
              )}
            </>
          )}
        </div>
      ) : (
        /* Post-analysis: tabbed dashboard */
        <div>
          {error && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700 mb-4">
              {typeof error === 'string' ? error : JSON.stringify(error)}
            </div>
          )}

          <TabContainer tabs={TAB_CONFIG} activeTab={activeTab} onTabChange={setActiveTab}>
            <div key="overview" data-tab="overview">
              <OverviewTab
                result={result}
                interpretation={interpretation}
                aiLoading={aiLoading}
                onSwitchToAI={() => setActiveTab('ai')}
              />
            </div>
            <div key="flow" data-tab="flow">
              <FlowTab result={result} />
            </div>
            <div key="ai" data-tab="ai">
              <AITab
                interpretation={interpretation}
                aiLoading={aiLoading}
                equipmentType={equipmentType}
                subtype={selectedSubtype}
                result={result}
              />
            </div>
            <div key="scenario" data-tab="scenario">
              <ScenarioTab
                equipmentType={equipmentType}
                subtype={selectedSubtype}
                baselineParams={baselineParams}
                fields={selectedSubtypeData?.fields || []}
                result={result}
              />
            </div>
          </TabContainer>

          <FloatingChat
            equipmentType={equipmentType}
            subtype={selectedSubtype}
            analysisData={result}
          />
        </div>
      )}
    </DashboardLayout>
  );
};

export default EquipmentAnalysis;
