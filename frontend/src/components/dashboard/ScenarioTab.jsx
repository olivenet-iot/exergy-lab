import { useState, useEffect } from 'react';
import { compareScenarios } from '../../services/api';
import ScenarioEditor from '../whatif/ScenarioEditor';
import ComparisonPanel from '../whatif/ComparisonPanel';

const ScenarioTab = ({ equipmentType, subtype, baselineParams, fields, result }) => {
  const [scenarioParams, setScenarioParams] = useState({ ...baselineParams });
  const [compareResult, setCompareResult] = useState(null);
  const [isComparing, setIsComparing] = useState(false);
  const [compareError, setCompareError] = useState(null);

  useEffect(() => {
    setScenarioParams({ ...baselineParams });
    setCompareResult(null);
    setCompareError(null);
  }, [baselineParams]);

  const handleScenarioParamChange = (fieldId, value) => {
    setScenarioParams((prev) => ({ ...prev, [fieldId]: value }));
  };

  const handleCompare = async () => {
    setIsComparing(true);
    setCompareError(null);
    try {
      const res = await compareScenarios({
        equipment_type: equipmentType,
        subtype,
        baseline_params: baselineParams,
        scenario_params: scenarioParams,
      });
      setCompareResult(res);
    } catch (err) {
      setCompareError(err.response?.data?.detail || 'Karşılaştırma hatası');
    } finally {
      setIsComparing(false);
    }
  };

  const handleCancel = () => {
    setScenarioParams({ ...baselineParams });
    setCompareResult(null);
    setCompareError(null);
  };

  return (
    <div className="space-y-6">
      <ScenarioEditor
        fields={fields || []}
        baselineParams={baselineParams}
        scenarioParams={scenarioParams}
        onParamChange={handleScenarioParamChange}
        onCompare={handleCompare}
        onCancel={handleCancel}
        isLoading={isComparing}
      />

      {compareError && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700">
          {typeof compareError === 'string' ? compareError : JSON.stringify(compareError)}
        </div>
      )}

      {compareResult && <ComparisonPanel compareResult={compareResult} />}

      {!compareResult && !isComparing && (
        <div className="text-center py-8 text-slate-400 text-sm">
          Parametreleri değiştirin ve karşılaştırma yapın.
        </div>
      )}
    </div>
  );
};

export default ScenarioTab;
