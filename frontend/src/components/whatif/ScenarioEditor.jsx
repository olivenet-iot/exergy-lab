const ScenarioEditor = ({ fields, baselineParams, scenarioParams, onParamChange, onCompare, onCancel, isLoading }) => {
  // Only show numeric fields that have a baseline value
  const editableFields = (fields || []).filter(f =>
    f.type === 'number' && baselineParams[f.name] != null
  );

  const handleReset = () => {
    editableFields.forEach(f => {
      onParamChange(f.name, baselineParams[f.name]);
    });
  };

  return (
    <div className="bg-amber-50 border border-amber-200 rounded-xl p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-amber-800">
          What-If Senaryo Modu
        </h3>
        <button
          onClick={onCancel}
          className="text-gray-400 hover:text-gray-600 text-xl leading-none"
          title="Kapat"
        >
          &times;
        </button>
      </div>

      <p className="text-sm text-amber-700 mb-4">
        Parametreleri degistirerek alternatif senaryolari karsilastirin.
      </p>

      <div className="space-y-4">
        {editableFields.map(field => {
          const baseVal = baselineParams[field.name];
          const scenVal = scenarioParams[field.name] ?? baseVal;
          const isChanged = Math.abs(scenVal - baseVal) > 1e-9;

          const sliderMin = field.min != null ? field.min : baseVal * 0.5;
          const sliderMax = field.max != null ? field.max : baseVal * 2;
          const step = baseVal >= 100 ? 1 : baseVal >= 1 ? 0.1 : 0.01;

          return (
            <div
              key={field.name}
              className={`p-3 rounded-lg ${isChanged ? 'bg-amber-100' : 'bg-white'}`}
            >
              <div className="flex items-center justify-between mb-1">
                <label className="text-sm font-medium text-gray-700">
                  {field.label}
                  {field.unit && <span className="text-gray-400 ml-1">({field.unit})</span>}
                </label>
                {isChanged && (
                  <span className="text-xs text-amber-600 font-mono">
                    {baseVal} &rarr; {scenVal}
                  </span>
                )}
              </div>
              <div className="flex items-center gap-3">
                <input
                  type="range"
                  min={sliderMin}
                  max={sliderMax}
                  step={step}
                  value={scenVal}
                  onChange={e => onParamChange(field.name, parseFloat(e.target.value))}
                  className="flex-1 accent-amber-500"
                />
                <input
                  type="number"
                  min={sliderMin}
                  max={sliderMax}
                  step={step}
                  value={scenVal}
                  onChange={e => onParamChange(field.name, parseFloat(e.target.value) || 0)}
                  className="w-24 px-2 py-1 text-sm border border-gray-300 rounded text-right font-mono focus:ring-amber-500 focus:border-amber-500"
                />
              </div>
            </div>
          );
        })}
      </div>

      <div className="flex items-center gap-3 mt-6">
        <button
          onClick={onCompare}
          disabled={isLoading}
          className="px-4 py-2 bg-amber-500 text-white rounded-lg hover:bg-amber-600 disabled:opacity-50 font-medium"
        >
          {isLoading ? 'Hesaplaniyor...' : 'Karsilastir'}
        </button>
        <button
          onClick={handleReset}
          className="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 font-medium"
        >
          Sifirla
        </button>
      </div>
    </div>
  );
};

export default ScenarioEditor;
