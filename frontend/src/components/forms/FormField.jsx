const FormField = ({ field, value, onChange }) => {
  const { id, label, unit, required, min, max, step, help, hint, default: defaultValue, type: fieldType, options } = field;

  const helpText = help || hint;

  // Select field
  if (fieldType === 'select' && options) {
    const firstValue = options[0]?.value ?? options[0] ?? '';
    return (
      <div className="space-y-1">
        <label htmlFor={id} className="block text-sm font-medium text-gray-700">
          {label}
          {required && <span className="text-red-500 ml-1">*</span>}
        </label>

        <select
          id={id}
          value={value ?? defaultValue ?? firstValue}
          onChange={(e) => onChange(e.target.value)}
          required={required}
          className="
            w-full px-3 py-2 rounded-lg border border-gray-300
            focus:ring-2 focus:ring-primary-500 focus:border-primary-500
            transition-colors duration-200 bg-white text-gray-900 shadow-sm
          "
        >
          {options.map((opt) => {
            const optValue = opt?.value ?? opt;
            const optLabel = opt?.label ?? opt;
            return <option key={optValue} value={optValue}>{optLabel}</option>;
          })}
        </select>

        {helpText && (
          <p className="text-xs text-gray-500">{helpText}</p>
        )}
      </div>
    );
  }

  // Boolean / checkbox field
  if (fieldType === 'boolean') {
    return (
      <div className="space-y-1">
        <label htmlFor={id} className="flex items-center gap-2 text-sm font-medium text-gray-700 cursor-pointer">
          <input
            id={id}
            type="checkbox"
            checked={value === true || value === 1}
            onChange={(e) => onChange(e.target.checked)}
            className="
              w-4 h-4 rounded border-gray-300 text-primary-600
              focus:ring-2 focus:ring-primary-500
            "
          />
          {label}
        </label>

        {helpText && (
          <p className="text-xs text-gray-500">{helpText}</p>
        )}
      </div>
    );
  }

  // Default: number field
  return (
    <div className="space-y-1">
      <label htmlFor={id} className="block text-sm font-medium text-gray-700">
        {label}
        {required && <span className="text-red-500 ml-1">*</span>}
        {unit && <span className="text-gray-400 ml-1">({unit})</span>}
      </label>

      <input
        id={id}
        type="number"
        value={value ?? defaultValue ?? ''}
        onChange={(e) => onChange(parseFloat(e.target.value) || null)}
        min={min}
        max={max}
        step={step || 'any'}
        required={required}
        className="
          w-full px-3 py-2 rounded-lg border border-gray-300
          focus:ring-2 focus:ring-primary-500 focus:border-primary-500
          transition-colors duration-200
        "
        placeholder={defaultValue ? `Varsayilan: ${defaultValue}` : ''}
      />

      {helpText && (
        <p className="text-xs text-gray-500">{helpText}</p>
      )}
    </div>
  );
};

export default FormField;
