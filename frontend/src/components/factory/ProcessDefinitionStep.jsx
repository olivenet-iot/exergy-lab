import { useState, useEffect } from 'react';
import { Flame, Thermometer, Snowflake, Cloud, Wind, Zap, Box, Factory, ArrowLeft } from 'lucide-react';
import { getProcessTypes, getProcessSubcategories } from '../../services/factoryApi';

const ICON_MAP = {
  drying: Flame,
  heating: Thermometer,
  cooling: Snowflake,
  steam_generation: Cloud,
  compressed_air: Wind,
  chp: Zap,
  cold_storage: Box,
  general_manufacturing: Factory,
};

const COLOR_MAP = {
  drying: 'text-orange-600 bg-orange-50 border-orange-200',
  heating: 'text-red-600 bg-red-50 border-red-200',
  cooling: 'text-cyan-600 bg-cyan-50 border-cyan-200',
  steam_generation: 'text-slate-600 bg-slate-50 border-slate-200',
  compressed_air: 'text-blue-600 bg-blue-50 border-blue-200',
  chp: 'text-yellow-600 bg-yellow-50 border-yellow-200',
  cold_storage: 'text-indigo-600 bg-indigo-50 border-indigo-200',
  general_manufacturing: 'text-emerald-600 bg-emerald-50 border-emerald-200',
};

const ProcessDefinitionStep = ({
  processType, setProcessType,
  processLabel, setProcessLabel,
  processParams, setProcessParams,
  processSubcategory, setProcessSubcategory,
  operatingHours, setOperatingHours,
  energyPrice, setEnergyPrice,
  skipProcess, setSkipProcess,
}) => {
  const [processTypes, setProcessTypes] = useState(null);
  const [subcategories, setSubcategories] = useState([]);
  const [loadingTypes, setLoadingTypes] = useState(true);
  const [loadingSubcats, setLoadingSubcats] = useState(false);

  // Fetch process types on mount
  useEffect(() => {
    getProcessTypes()
      .then((data) => setProcessTypes(data.process_types))
      .catch(() => setProcessTypes({}))
      .finally(() => setLoadingTypes(false));
  }, []);

  // Fetch subcategories when processType changes
  useEffect(() => {
    if (!processType) {
      setSubcategories([]);
      return;
    }
    setLoadingSubcats(true);
    getProcessSubcategories(processType)
      .then((data) => {
        setSubcategories(data.subcategories || []);
        // Set default subcategory if not already set
        if (!processSubcategory || processSubcategory === 'general') {
          const hasGeneral = (data.subcategories || []).some((s) => s.key === 'general');
          if (hasGeneral) setProcessSubcategory('general');
          else if (data.subcategories?.length) setProcessSubcategory(data.subcategories[0].key);
        }
      })
      .catch(() => setSubcategories([]))
      .finally(() => setLoadingSubcats(false));
  }, [processType]);

  const handleParamChange = (paramName, value) => {
    setProcessParams((prev) => ({ ...prev, [paramName]: value }));
  };

  const handleTypeSelect = (typeKey) => {
    setProcessType(typeKey);
    setProcessParams({});
    setProcessSubcategory('general');
  };

  const handleChangeType = () => {
    setProcessType(null);
    setProcessParams({});
    setProcessSubcategory('general');
    setSubcategories([]);
  };

  if (loadingTypes) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-indigo-600" />
      </div>
    );
  }

  // Phase 1: Type selection grid
  if (!processType) {
    const typeEntries = Object.entries(processTypes || {});
    return (
      <div className="space-y-6">
        <div>
          <p className="text-sm text-gray-600 mb-4">
            Fabrikanızın ana prosesini seçin. Bu bilgi, termodinamik ideal ve en iyi teknoloji (BAT) ile karşılaştırma yapılmasını sağlar.
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {typeEntries.map(([key, info]) => {
              const Icon = ICON_MAP[key] || Factory;
              const color = COLOR_MAP[key] || 'text-gray-600 bg-gray-50 border-gray-200';
              return (
                <button
                  key={key}
                  onClick={() => !skipProcess && handleTypeSelect(key)}
                  disabled={skipProcess}
                  className={`flex items-start gap-3 p-4 rounded-lg border transition-colors text-left ${
                    skipProcess
                      ? 'opacity-50 cursor-not-allowed border-gray-200'
                      : 'hover:border-indigo-300 border-gray-200 hover:shadow-sm'
                  }`}
                >
                  <div className={`p-2 rounded-lg flex-shrink-0 ${color}`}>
                    <Icon className="w-5 h-5" />
                  </div>
                  <div className="min-w-0">
                    <div className="font-medium text-gray-900 text-sm">{info.label}</div>
                    <div className="text-xs text-gray-500 mt-0.5">{info.description}</div>
                  </div>
                </button>
              );
            })}
          </div>
        </div>

        <label className="flex items-center gap-2 cursor-pointer pt-2 border-t border-gray-100">
          <input
            type="checkbox"
            checked={skipProcess}
            onChange={(e) => setSkipProcess(e.target.checked)}
            className="rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
          />
          <span className="text-sm text-gray-600">Proses tanımı olmadan devam et</span>
        </label>
      </div>
    );
  }

  // Phase 2: Parameter form
  const typeInfo = processTypes?.[processType];
  if (!typeInfo) return null;

  const Icon = ICON_MAP[processType] || Factory;
  const color = COLOR_MAP[processType] || 'text-gray-600 bg-gray-50 border-gray-200';
  const paramDefs = typeInfo.param_definitions || {};
  const requiredParams = typeInfo.required_params || [];
  const optionalParams = typeInfo.optional_params || {};

  return (
    <div className="space-y-6">
      {/* Selected type header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className={`p-2 rounded-lg ${color}`}>
            <Icon className="w-5 h-5" />
          </div>
          <div>
            <div className="font-medium text-gray-900">{typeInfo.label}</div>
            <div className="text-xs text-gray-500">{typeInfo.description}</div>
          </div>
        </div>
        <button
          onClick={handleChangeType}
          className="flex items-center gap-1 text-sm text-indigo-600 hover:text-indigo-800"
        >
          <ArrowLeft className="w-3 h-3" />
          Değiştir
        </button>
      </div>

      {/* Subcategory dropdown */}
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">Alt Kategori</label>
        {loadingSubcats ? (
          <div className="flex items-center gap-2 py-2">
            <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-indigo-600" />
            <span className="text-sm text-gray-500">Yükleniyor...</span>
          </div>
        ) : (
          <select
            value={processSubcategory}
            onChange={(e) => setProcessSubcategory(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white"
          >
            {subcategories.map((sc) => (
              <option key={sc.key} value={sc.key}>
                {sc.label}
              </option>
            ))}
          </select>
        )}
        {subcategories.find((sc) => sc.key === processSubcategory)?.source && (
          <p className="text-xs text-gray-400 mt-1">
            Kaynak: {subcategories.find((sc) => sc.key === processSubcategory).source}
          </p>
        )}
      </div>

      {/* Process description */}
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">Proses Açıklaması</label>
        <textarea
          value={processLabel}
          onChange={(e) => setProcessLabel(e.target.value)}
          placeholder="Örnek: Ana üretim hattı kurutma prosesi"
          rows={2}
          className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
        />
      </div>

      {/* Required parameters */}
      <div>
        <h4 className="text-sm font-medium text-gray-800 mb-3">Proses Parametreleri</h4>
        <div className="space-y-3">
          {requiredParams.map((paramKey) => {
            const def = paramDefs[paramKey];
            if (!def) return null;
            return (
              <div key={paramKey}>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  {def.label}
                  <span className="text-red-500 ml-1">*</span>
                  {def.unit && <span className="text-gray-400 ml-1">({def.unit})</span>}
                </label>
                <input
                  type="number"
                  value={processParams[paramKey] ?? ''}
                  onChange={(e) => handleParamChange(paramKey, e.target.value)}
                  min={def.min}
                  max={def.max}
                  step="any"
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>
            );
          })}
        </div>
      </div>

      {/* Optional parameters */}
      {Object.keys(optionalParams).length > 0 && (
        <div>
          <h4 className="text-sm font-medium text-gray-800 mb-3">Ek Parametreler <span className="text-gray-400 font-normal">(opsiyonel)</span></h4>
          <div className="space-y-3">
            {Object.entries(optionalParams).map(([paramKey, info]) => (
              <div key={paramKey}>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  {info.label}
                  {info.type === 'float' && <span className="text-gray-400 ml-1">({info.default != null ? `varsayılan: ${info.default}` : ''})</span>}
                </label>
                {info.type === 'str' ? (
                  <input
                    type="text"
                    value={processParams[paramKey] ?? ''}
                    onChange={(e) => handleParamChange(paramKey, e.target.value)}
                    placeholder={info.default || ''}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                  />
                ) : (
                  <input
                    type="number"
                    value={processParams[paramKey] ?? ''}
                    onChange={(e) => handleParamChange(paramKey, e.target.value)}
                    placeholder={info.default != null ? String(info.default) : ''}
                    step="any"
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                  />
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Economic parameters */}
      <div className="border-t border-gray-100 pt-4">
        <h4 className="text-sm font-medium text-gray-800 mb-3">Ekonomik Parametreler</h4>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Yıllık Çalışma Saati <span className="text-gray-400">(saat/yıl)</span>
            </label>
            <input
              type="number"
              value={operatingHours}
              onChange={(e) => setOperatingHours(Number(e.target.value) || 0)}
              min={0}
              max={8760}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Enerji Fiyatı <span className="text-gray-400">(EUR/kWh)</span>
            </label>
            <input
              type="number"
              value={energyPrice}
              onChange={(e) => setEnergyPrice(Number(e.target.value) || 0)}
              min={0}
              step="0.01"
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>
        </div>
      </div>
    </div>
  );
};

/**
 * Validates the process definition step.
 * Returns true if skipProcess is checked, or if all required params are filled.
 */
export const validateProcessStep = (processType, processParams, skipProcess, processTypes) => {
  if (skipProcess) return true;
  if (!processType || !processTypes?.[processType]) return false;

  const typeInfo = processTypes[processType];
  const requiredParams = typeInfo.required_params || [];
  const paramDefs = typeInfo.param_definitions || {};

  for (const paramKey of requiredParams) {
    const val = processParams[paramKey];
    if (val == null || val === '') return false;
    const num = Number(val);
    if (isNaN(num)) return false;
    const def = paramDefs[paramKey];
    if (def?.min != null && num < def.min) return false;
    if (def?.max != null && num > def.max) return false;
  }
  return true;
};

export default ProcessDefinitionStep;
