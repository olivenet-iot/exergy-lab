import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Wind, Flame, Snowflake, Droplets, ArrowLeftRight, Zap, Sun } from 'lucide-react';
import { getEquipmentConfig, compareScenarios } from '../services/api';
import { useAnalysis } from '../hooks/useAnalysis';
import SubtypeSelector from '../components/equipment/SubtypeSelector';
import ParameterForm from '../components/forms/ParameterForm';
import ResultsPanel from '../components/results/ResultsPanel';
import SolutionsList from '../components/results/SolutionsList';
import AIInterpretation from '../components/results/AIInterpretation';
import ScenarioEditor from '../components/whatif/ScenarioEditor';
import ComparisonPanel from '../components/whatif/ComparisonPanel';
import Card from '../components/common/Card';
import LoadingSpinner from '../components/common/Loading';

const EQUIPMENT_META = {
  compressor: { name: 'Kompresör', icon: Wind, color: 'text-blue-600' },
  boiler: { name: 'Kazan', icon: Flame, color: 'text-orange-600' },
  chiller: { name: 'Chiller', icon: Snowflake, color: 'text-cyan-600' },
  pump: { name: 'Pompa', icon: Droplets, color: 'text-emerald-600' },
  heat_exchanger: { name: 'Isı Eşanjörü', icon: ArrowLeftRight, color: 'text-purple-600' },
  steam_turbine: { name: 'Buhar Türbini', icon: Zap, color: 'text-yellow-600' },
  dryer: { name: 'Kurutma Fırını', icon: Sun, color: 'text-red-600' },
};

const EquipmentAnalysis = () => {
  const { equipmentType } = useParams();
  const meta = EQUIPMENT_META[equipmentType] || { name: equipmentType, icon: Wind, color: 'text-gray-600' };
  const Icon = meta.icon;

  const [subtypes, setSubtypes] = useState([]);
  const [subtypesLoading, setSubtypesLoading] = useState(true);
  const [selectedSubtype, setSelectedSubtype] = useState(null);
  const [formValues, setFormValues] = useState({});

  const { result, solutions, loading, error, analyze, reset, interpretation, aiLoading } = useAnalysis();

  // What-If state
  const [whatIfMode, setWhatIfMode] = useState(false);
  const [baselineParams, setBaselineParams] = useState({});
  const [scenarioParams, setScenarioParams] = useState({});
  const [compareResult, setCompareResult] = useState(null);
  const [isComparing, setIsComparing] = useState(false);
  const [compareError, setCompareError] = useState(null);

  // Fetch subtypes with field definitions when equipment type changes
  useEffect(() => {
    setSubtypes([]);
    setSelectedSubtype(null);
    setFormValues({});
    setWhatIfMode(false);
    setCompareResult(null);
    setCompareError(null);
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
    setWhatIfMode(false);
    setCompareResult(null);
    setCompareError(null);
    reset();
  };

  const handleFormChange = (fieldId, value) => {
    setFormValues((prev) => ({ ...prev, [fieldId]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setWhatIfMode(false);
    setCompareResult(null);
    setCompareError(null);
    analyze(equipmentType, selectedSubtype, formValues);
    setBaselineParams({ ...formValues });
  };

  const handleWhatIfToggle = () => {
    setWhatIfMode(true);
    setScenarioParams({ ...baselineParams });
    setCompareResult(null);
    setCompareError(null);
  };

  const handleWhatIfCancel = () => {
    setWhatIfMode(false);
    setCompareResult(null);
    setCompareError(null);
  };

  const handleScenarioParamChange = (fieldId, value) => {
    setScenarioParams(prev => ({ ...prev, [fieldId]: value }));
  };

  const handleCompare = async () => {
    setIsComparing(true);
    setCompareError(null);
    try {
      const res = await compareScenarios({
        equipment_type: equipmentType,
        subtype: selectedSubtype,
        baseline_params: baselineParams,
        scenario_params: scenarioParams,
      });
      setCompareResult(res);
    } catch (err) {
      setCompareError(err.response?.data?.detail || 'Karsilastirma hatasi');
    } finally {
      setIsComparing(false);
    }
  };

  const selectedSubtypeData = subtypes?.find((t) => (t.id || t.type) === selectedSubtype);

  return (
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

      {/* Parameter form + analysis for ALL equipment types */}
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

          {result && (
            <>
              <div className="border-t border-gray-200 pt-8">
                <h2 className="text-2xl font-bold text-gray-900 mb-6">Analiz Sonuçları</h2>
                <ResultsPanel data={result} />
              </div>

              <AIInterpretation interpretation={interpretation} loading={aiLoading} />

              {!interpretation && !aiLoading && solutions.length > 0 && (
                <SolutionsList solutions={solutions} />
              )}

              {/* What-If Scenario Mode */}
              {!whatIfMode && (
                <div className="flex justify-center">
                  <button
                    onClick={handleWhatIfToggle}
                    className="px-6 py-3 bg-amber-500 text-white rounded-lg hover:bg-amber-600 font-medium shadow-sm"
                  >
                    What-If Senaryo Modu
                  </button>
                </div>
              )}

              {whatIfMode && (
                <div className="space-y-6">
                  <ScenarioEditor
                    fields={selectedSubtypeData?.fields || []}
                    baselineParams={baselineParams}
                    scenarioParams={scenarioParams}
                    onParamChange={handleScenarioParamChange}
                    onCompare={handleCompare}
                    onCancel={handleWhatIfCancel}
                    isLoading={isComparing}
                  />

                  {compareError && (
                    <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700">
                      {typeof compareError === 'string' ? compareError : JSON.stringify(compareError)}
                    </div>
                  )}

                  {compareResult && (
                    <ComparisonPanel compareResult={compareResult} />
                  )}
                </div>
              )}
            </>
          )}
        </>
      )}
    </div>
  );
};

export default EquipmentAnalysis;
