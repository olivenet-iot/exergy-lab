const FormField = ({ field, value, onChange }) => {
  const { id, label, unit, required, min, max, step, help, default: defaultValue, type: fieldType, options } = field;

  // Select field
  if (fieldType === 'select' && options) {
    return (
      <div className="space-y-1">
        <label htmlFor={id} className="block text-sm font-medium text-gray-700">
          {label}
          {required && <span className="text-red-500 ml-1">*</span>}
        </label>

        <select
          id={id}
          value={value ?? defaultValue ?? options[0] ?? ''}
          onChange={(e) => onChange(e.target.value)}
          required={required}
          className="
            w-full px-3 py-2 rounded-lg border border-gray-300
            focus:ring-2 focus:ring-primary-500 focus:border-primary-500
            transition-colors duration-200 bg-white
          "
        >
          {options.map((opt) => (
            <option key={opt} value={opt}>{opt}</option>
          ))}
        </select>

        {help && (
          <p className="text-xs text-gray-500">{help}</p>
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

        {help && (
          <p className="text-xs text-gray-500">{help}</p>
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

      {help && (
        <p className="text-xs text-gray-500">{help}</p>
      )}
    </div>
  );
};

export default FormField;
