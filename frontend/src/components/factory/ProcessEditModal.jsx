import { useState } from 'react';
import { X, Check } from 'lucide-react';
import { updateProjectProcess } from '../../services/factoryApi';
import ProcessDefinitionStep from './ProcessDefinitionStep';

const ProcessEditModal = ({ projectId, onClose, onSuccess }) => {
  const [processType, setProcessType] = useState(null);
  const [processLabel, setProcessLabel] = useState('');
  const [processParams, setProcessParams] = useState({});
  const [processSubcategory, setProcessSubcategory] = useState('general');
  const [operatingHours, setOperatingHours] = useState(6000);
  const [energyPrice, setEnergyPrice] = useState(0.08);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);

  // skipProcess not applicable here — user explicitly chose to add
  const skipDummy = false;
  const setSkipDummy = () => {};

  const handleSave = async () => {
    if (!processType) {
      setError('Lütfen bir proses tipi seçin');
      return;
    }

    setSaving(true);
    setError(null);

    try {
      const cleanedParams = {};
      for (const [k, v] of Object.entries(processParams)) {
        if (v != null && v !== '') {
          const num = Number(v);
          cleanedParams[k] = isNaN(num) ? v : num;
        }
      }

      await updateProjectProcess(projectId, {
        process_type: processType,
        process_label: processLabel || '',
        process_parameters: cleanedParams,
        process_subcategory: processSubcategory,
        operating_hours: operatingHours,
        energy_price_eur_kwh: energyPrice,
      });

      onSuccess();
    } catch (err) {
      setError(err?.response?.data?.detail || 'Proses tanımı kaydedilemedi');
      setSaving(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-xl shadow-xl w-full max-w-2xl max-h-[85vh] flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-gray-200">
          <h3 className="text-lg font-semibold text-gray-900">Proses Tanımı Ekle</h3>
          <button onClick={onClose} className="p-1 hover:bg-gray-100 rounded-lg transition-colors">
            <X className="w-5 h-5 text-gray-500" />
          </button>
        </div>

        {/* Body */}
        <div className="flex-1 overflow-y-auto px-6 py-4">
          <ProcessDefinitionStep
            processType={processType}
            setProcessType={setProcessType}
            processLabel={processLabel}
            setProcessLabel={setProcessLabel}
            processParams={processParams}
            setProcessParams={setProcessParams}
            processSubcategory={processSubcategory}
            setProcessSubcategory={setProcessSubcategory}
            operatingHours={operatingHours}
            setOperatingHours={setOperatingHours}
            energyPrice={energyPrice}
            setEnergyPrice={setEnergyPrice}
            skipProcess={skipDummy}
            setSkipProcess={setSkipDummy}
          />

          {error && (
            <div className="mt-4 bg-red-50 border border-red-200 rounded-lg p-3 text-sm text-red-700">
              {error}
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="flex items-center justify-end gap-3 px-6 py-4 border-t border-gray-200">
          <button
            onClick={onClose}
            className="px-4 py-2 text-gray-600 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
          >
            İptal
          </button>
          <button
            onClick={handleSave}
            disabled={saving || !processType}
            className="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors disabled:opacity-50"
          >
            {saving ? (
              <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white" />
            ) : (
              <Check className="w-4 h-4" />
            )}
            Kaydet
          </button>
        </div>
      </div>
    </div>
  );
};

export default ProcessEditModal;
