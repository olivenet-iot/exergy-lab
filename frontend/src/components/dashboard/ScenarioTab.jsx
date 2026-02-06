import { useState, useEffect } from 'react';
import { TrendingUp, TrendingDown, Minus } from 'lucide-react';
import { compareScenarios } from '../../services/api';
import { formatNumber } from '../../utils/formatters';
import ScenarioEditor from '../whatif/ScenarioEditor';
import ComparisonPanel from '../whatif/ComparisonPanel';

const DeltaCard = ({ label, value, unit, isPositive }) => {
  const color = value === 0
    ? 'bg-gray-50 border-gray-200 text-gray-600'
    : isPositive
      ? 'bg-emerald-50 border-emerald-200 text-emerald-700'
      : 'bg-red-50 border-red-200 text-red-700';

  const Icon = value === 0 ? Minus : isPositive ? TrendingUp : TrendingDown;
  const sign = value > 0 ? '+' : '';

  return (
    <div className={`rounded-lg border p-4 ${color}`}>
      <div className="flex items-center gap-2 mb-1">
        <Icon className="w-4 h-4" />
        <span className="text-xs font-medium uppercase tracking-wider opacity-75">{label}</span>
      </div>
      <p className="text-lg font-bold font-mono">
        {sign}{formatNumber(value)} {unit}
      </p>
    </div>
  );
};

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
      setCompareError(err.response?.data?.detail || 'Karsilastirma hatasi');
    } finally {
      setIsComparing(false);
    }
  };

  const handleCancel = () => {
    setScenarioParams({ ...baselineParams });
    setCompareResult(null);
    setCompareError(null);
  };

  // Compute deltas when compareResult exists
  const deltas = compareResult ? (() => {
    const baseM = compareResult.baseline?.metrics || {};
    const scenM = compareResult.scenario?.metrics || {};

    const effDelta = (scenM.exergy_efficiency_percent ?? 0) - (baseM.exergy_efficiency_percent ?? 0);
    const annualDelta = (baseM.annual_loss_kWh ?? 0) - (scenM.annual_loss_kWh ?? 0);
    const costDelta = (baseM.annual_cost_eur ?? 0) - (scenM.annual_cost_eur ?? 0);

    return { effDelta, annualDelta, costDelta };
  })() : null;

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

      {/* Delta summary cards */}
      {compareResult && deltas && (
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <DeltaCard
            label="Verim Degisimi"
            value={deltas.effDelta}
            unit="%"
            isPositive={deltas.effDelta > 0}
          />
          <DeltaCard
            label="Yillik Tasarruf"
            value={deltas.annualDelta}
            unit="kWh"
            isPositive={deltas.annualDelta > 0}
          />
          <DeltaCard
            label="Maliyet Tasarrufu"
            value={deltas.costDelta}
            unit="EUR"
            isPositive={deltas.costDelta > 0}
          />
        </div>
      )}

      {compareResult && <ComparisonPanel compareResult={compareResult} />}

      {!compareResult && !isComparing && (
        <div className="text-center py-8 text-slate-400 text-sm">
          Parametreleri degistirin ve karsilastirma yapin.
        </div>
      )}
    </div>
  );
};

export default ScenarioTab;
