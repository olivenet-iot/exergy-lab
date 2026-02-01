import { useState, useEffect } from 'react';
import { X, ArrowRight, ArrowLeft, Check, Wind, Flame, Snowflake, Droplets } from 'lucide-react';
import { getEquipmentConfig } from '../../services/api';

const EQUIPMENT_TYPES = [
  { id: 'compressor', label: 'Kompresor', icon: Wind, color: 'text-blue-600 bg-blue-50 border-blue-200' },
  { id: 'boiler', label: 'Kazan', icon: Flame, color: 'text-orange-600 bg-orange-50 border-orange-200' },
  { id: 'chiller', label: 'Chiller', icon: Snowflake, color: 'text-cyan-600 bg-cyan-50 border-cyan-200' },
  { id: 'pump', label: 'Pompa', icon: Droplets, color: 'text-emerald-600 bg-emerald-50 border-emerald-200' },
];

const AddEquipmentModal = ({ onAdd, onClose }) => {
  const [step, setStep] = useState(1);
  const [selectedType, setSelectedType] = useState(null);
  const [subtypes, setSubtypes] = useState([]);
  const [selectedSubtype, setSelectedSubtype] = useState(null);
  const [fields, setFields] = useState([]);
  const [formValues, setFormValues] = useState({});
  const [name, setName] = useState('');
  const [loading, setLoading] = useState(false);

  // Fetch subtypes when type is selected
  useEffect(() => {
    if (!selectedType) return;
    setLoading(true);
    getEquipmentConfig(selectedType)
      .then((data) => {
        setSubtypes(data);
        setLoading(false);
      })
      .catch(() => {
        setSubtypes([]);
        setLoading(false);
      });
  }, [selectedType]);

  // Set fields when subtype is selected
  useEffect(() => {
    if (!selectedSubtype || !subtypes.length) return;
    const st = subtypes.find((s) => s.id === selectedSubtype);
    if (st) {
      setFields(st.fields || []);
      // Set default values
      const defaults = {};
      (st.fields || []).forEach((f) => {
        if (f.default != null) defaults[f.name] = f.default;
      });
      setFormValues(defaults);
    }
  }, [selectedSubtype, subtypes]);

  const handleFieldChange = (fieldName, value) => {
    setFormValues((prev) => ({ ...prev, [fieldName]: value }));
  };

  const handleConfirm = () => {
    // Build parameters (only non-empty values)
    const parameters = {};
    for (const f of fields) {
      const val = formValues[f.name];
      if (val != null && val !== '') {
        if (f.type === 'number') {
          parameters[f.name] = Number(val);
        } else if (f.type === 'boolean') {
          parameters[f.name] = Boolean(val);
        } else {
          parameters[f.name] = val;
        }
      }
    }

    const equipmentName = name.trim() || `${selectedType}-${Date.now().toString().slice(-4)}`;

    onAdd({
      type: selectedType,
      subtype: selectedSubtype,
      name: equipmentName,
      parameters,
    });
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-xl shadow-xl w-full max-w-lg max-h-[80vh] flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-gray-200">
          <h3 className="text-lg font-semibold text-gray-900">Ekipman Ekle (Adim {step}/3)</h3>
          <button onClick={onClose} className="p-1 hover:bg-gray-100 rounded-lg transition-colors">
            <X className="w-5 h-5 text-gray-500" />
          </button>
        </div>

        {/* Body */}
        <div className="flex-1 overflow-y-auto px-6 py-4">
          {/* Step 1: Select type */}
          {step === 1 && (
            <div className="space-y-3">
              <p className="text-sm text-gray-600 mb-4">Ekipman tipini secin:</p>
              {EQUIPMENT_TYPES.map((type) => {
                const Icon = type.icon;
                return (
                  <button
                    key={type.id}
                    onClick={() => {
                      setSelectedType(type.id);
                      setSelectedSubtype(null);
                      setFields([]);
                      setFormValues({});
                      setStep(2);
                    }}
                    className={`w-full flex items-center gap-3 p-3 rounded-lg border transition-colors hover:border-indigo-300 ${
                      selectedType === type.id ? 'border-indigo-500 bg-indigo-50' : 'border-gray-200'
                    }`}
                  >
                    <div className={`p-2 rounded-lg ${type.color}`}>
                      <Icon className="w-5 h-5" />
                    </div>
                    <span className="font-medium text-gray-900">{type.label}</span>
                  </button>
                );
              })}
            </div>
          )}

          {/* Step 2: Select subtype */}
          {step === 2 && (
            <div className="space-y-3">
              <p className="text-sm text-gray-600 mb-4">Alt tipi secin:</p>
              {loading ? (
                <div className="flex items-center justify-center py-8">
                  <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-indigo-600" />
                </div>
              ) : (
                subtypes.map((st) => (
                  <button
                    key={st.id}
                    onClick={() => {
                      setSelectedSubtype(st.id);
                      setStep(3);
                    }}
                    className={`w-full text-left p-3 rounded-lg border transition-colors hover:border-indigo-300 ${
                      selectedSubtype === st.id ? 'border-indigo-500 bg-indigo-50' : 'border-gray-200'
                    }`}
                  >
                    <div className="font-medium text-gray-900">{st.name}</div>
                    {st.description && (
                      <div className="text-xs text-gray-500 mt-0.5">{st.description}</div>
                    )}
                  </button>
                ))
              )}
            </div>
          )}

          {/* Step 3: Parameters */}
          {step === 3 && (
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Ekipman Adi</label>
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder={`Ornek: ${selectedType}-1`}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>

              {fields.map((field) => (
                <div key={field.name}>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    {field.label}
                    {field.required && <span className="text-red-500 ml-1">*</span>}
                    {field.unit && <span className="text-gray-400 ml-1">({field.unit})</span>}
                  </label>
                  {field.type === 'select' ? (
                    <select
                      value={formValues[field.name] ?? field.default ?? ''}
                      onChange={(e) => handleFieldChange(field.name, e.target.value)}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                    >
                      {(field.options || []).map((opt) => (
                        <option key={opt} value={opt}>{opt}</option>
                      ))}
                    </select>
                  ) : field.type === 'boolean' ? (
                    <label className="flex items-center gap-2 cursor-pointer">
                      <input
                        type="checkbox"
                        checked={!!formValues[field.name]}
                        onChange={(e) => handleFieldChange(field.name, e.target.checked)}
                        className="rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                      />
                      <span className="text-sm text-gray-600">Evet</span>
                    </label>
                  ) : (
                    <input
                      type="number"
                      value={formValues[field.name] ?? ''}
                      onChange={(e) => handleFieldChange(field.name, e.target.value)}
                      placeholder={field.default != null ? String(field.default) : ''}
                      min={field.min}
                      max={field.max}
                      step="any"
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                    />
                  )}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="flex items-center justify-between px-6 py-4 border-t border-gray-200">
          {step > 1 ? (
            <button
              onClick={() => setStep(step - 1)}
              className="flex items-center gap-1 px-3 py-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <ArrowLeft className="w-4 h-4" />
              Geri
            </button>
          ) : (
            <div />
          )}

          {step === 3 && (
            <button
              onClick={handleConfirm}
              className="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors"
            >
              <Check className="w-4 h-4" />
              Ekle
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default AddEquipmentModal;
