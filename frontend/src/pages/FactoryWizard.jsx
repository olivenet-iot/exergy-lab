import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Factory, ArrowLeft, ArrowRight, Plus, Trash2, Check } from 'lucide-react';
import { createFactoryProject, addEquipmentToProject, getProcessTypes } from '../services/factoryApi';
import { getEquipmentConfig } from '../services/api';
import Card from '../components/common/Card';
import AddEquipmentModal from '../components/factory/AddEquipmentModal';
import ProcessDefinitionStep, { validateProcessStep } from '../components/factory/ProcessDefinitionStep';

const SECTORS = [
  { value: 'textile', label: 'Tekstil' },
  { value: 'food', label: 'Gıda' },
  { value: 'chemical', label: 'Kimya' },
  { value: 'metal', label: 'Metal' },
  { value: 'cement', label: 'Çimento' },
  { value: 'paper', label: 'Kağıt' },
  { value: 'automotive', label: 'Otomotiv' },
];

const EQUIPMENT_TYPE_LABELS = {
  compressor: 'Kompresör',
  boiler: 'Kazan',
  chiller: 'Chiller',
  pump: 'Pompa',
  heat_exchanger: 'Isı Eşanjörü',
  steam_turbine: 'Buhar Türbini',
  dryer: 'Kurutma Fırını',
};

const FactoryWizard = () => {
  const navigate = useNavigate();
  const [step, setStep] = useState(1);

  // Step 1: Project info
  const [name, setName] = useState('');
  const [sector, setSector] = useState('');
  const [description, setDescription] = useState('');

  // Step 2: Process definition
  const [processType, setProcessType] = useState(null);
  const [processLabel, setProcessLabel] = useState('');
  const [processParams, setProcessParams] = useState({});
  const [processSubcategory, setProcessSubcategory] = useState('general');
  const [operatingHours, setOperatingHours] = useState(6000);
  const [energyPrice, setEnergyPrice] = useState(0.08);
  const [skipProcess, setSkipProcess] = useState(false);
  const [processTypesData, setProcessTypesData] = useState(null);

  // Step 3: Equipment
  const [equipment, setEquipment] = useState([]);
  const [showModal, setShowModal] = useState(false);

  // State
  const [creating, setCreating] = useState(false);
  const [error, setError] = useState(null);

  // Fetch process types for validation
  useEffect(() => {
    getProcessTypes()
      .then((data) => setProcessTypesData(data.process_types))
      .catch(() => {});
  }, []);

  const handleAddEquipment = (eq) => {
    setEquipment((prev) => [...prev, { ...eq, _tempId: Date.now().toString() }]);
    setShowModal(false);
  };

  const handleRemoveEquipment = (tempId) => {
    setEquipment((prev) => prev.filter((eq) => eq._tempId !== tempId));
  };

  const handleStep2Continue = () => {
    if (!skipProcess && !validateProcessStep(processType, processParams, skipProcess, processTypesData)) {
      setError('Lütfen tüm zorunlu proses parametrelerini doldurun');
      return;
    }
    setError(null);
    setStep(3);
  };

  const handleCreate = async () => {
    if (!name.trim()) {
      setError('Proje adı gereklidir');
      return;
    }
    if (equipment.length === 0) {
      setError('En az bir ekipman ekleyin');
      return;
    }

    setCreating(true);
    setError(null);

    try {
      // Build process params — convert numeric strings to numbers
      const cleanedParams = {};
      for (const [k, v] of Object.entries(processParams)) {
        if (v != null && v !== '') {
          const num = Number(v);
          cleanedParams[k] = isNaN(num) ? v : num;
        }
      }

      // Create project with process fields
      const projectResp = await createFactoryProject(name, sector || null, description || null, {
        process_type: skipProcess ? null : processType,
        process_label: skipProcess ? null : (processLabel || null),
        process_parameters: skipProcess ? null : cleanedParams,
        process_subcategory: skipProcess ? null : processSubcategory,
        operating_hours: operatingHours,
        energy_price_eur_kwh: energyPrice,
      });
      const projectId = projectResp.project.id;

      // Add equipment
      for (const eq of equipment) {
        await addEquipmentToProject(projectId, {
          type: eq.type,
          subtype: eq.subtype,
          name: eq.name,
          parameters: eq.parameters,
        });
      }

      // Navigate to dashboard
      navigate(`/factory/${projectId}`);
    } catch (err) {
      setError(err?.response?.data?.detail || 'Proje oluşturulamadı');
      setCreating(false);
    }
  };

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex items-center gap-3">
        <button
          onClick={() => navigate('/factory')}
          className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
        >
          <ArrowLeft className="w-5 h-5 text-gray-600" />
        </button>
        <Factory className="w-8 h-8 text-indigo-600" />
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Yeni Fabrika Projesi</h2>
          <p className="text-gray-600 mt-1">Adım {step} / 3</p>
        </div>
      </div>

      {/* Step indicator */}
      <div className="flex items-center gap-4">
        <div className={`flex items-center gap-2 px-3 py-1 rounded-full text-sm font-medium ${step >= 1 ? 'bg-indigo-100 text-indigo-700' : 'bg-gray-100 text-gray-500'}`}>
          <span className="w-5 h-5 rounded-full bg-indigo-600 text-white flex items-center justify-center text-xs">1</span>
          Proje Bilgileri
        </div>
        <div className="w-8 h-0.5 bg-gray-300" />
        <div className={`flex items-center gap-2 px-3 py-1 rounded-full text-sm font-medium ${step >= 2 ? 'bg-indigo-100 text-indigo-700' : 'bg-gray-100 text-gray-500'}`}>
          <span className={`w-5 h-5 rounded-full flex items-center justify-center text-xs ${step >= 2 ? 'bg-indigo-600 text-white' : 'bg-gray-300 text-gray-600'}`}>2</span>
          Proses Tanımı
        </div>
        <div className="w-8 h-0.5 bg-gray-300" />
        <div className={`flex items-center gap-2 px-3 py-1 rounded-full text-sm font-medium ${step >= 3 ? 'bg-indigo-100 text-indigo-700' : 'bg-gray-100 text-gray-500'}`}>
          <span className={`w-5 h-5 rounded-full flex items-center justify-center text-xs ${step >= 3 ? 'bg-indigo-600 text-white' : 'bg-gray-300 text-gray-600'}`}>3</span>
          Ekipman Envanteri
        </div>
      </div>

      {/* Step 1: Project info */}
      {step === 1 && (
        <Card title="Proje Bilgileri">
          <div className="space-y-4 max-w-lg">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Proje Adı *</label>
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Örnek: ABC Tekstil Fabrikası"
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Sektör</label>
              <select
                value={sector}
                onChange={(e) => setSector(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
              >
                <option value="">Sektör seçin...</option>
                {SECTORS.map((s) => (
                  <option key={s.value} value={s.value}>{s.label}</option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Açıklama</label>
              <textarea
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="Proje hakkında kısa açıklama..."
                rows={3}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
              />
            </div>

            <div className="flex justify-end pt-4">
              <button
                onClick={() => {
                  if (!name.trim()) {
                    setError('Proje adı gereklidir');
                    return;
                  }
                  setError(null);
                  setStep(2);
                }}
                className="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors"
              >
                Devam
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </Card>
      )}

      {/* Step 2: Process definition */}
      {step === 2 && (
        <>
          <Card title="Proses Tanımı">
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
              skipProcess={skipProcess}
              setSkipProcess={setSkipProcess}
            />
          </Card>

          <div className="flex items-center justify-between">
            <button
              onClick={() => setStep(1)}
              className="flex items-center gap-2 px-4 py-2 text-gray-600 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
            >
              <ArrowLeft className="w-4 h-4" />
              Geri
            </button>
            <button
              onClick={handleStep2Continue}
              className="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors"
            >
              Devam
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </>
      )}

      {/* Step 3: Equipment inventory */}
      {step === 3 && (
        <>
          <Card title="Ekipman Envanteri">
            {equipment.length === 0 ? (
              <div className="text-center py-8 text-gray-500">
                <p>Henüz ekipman eklenmedi. Analiz için en az bir ekipman ekleyin.</p>
              </div>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b border-gray-200">
                      <th className="text-left py-2 px-3 text-gray-600 font-medium">Ad</th>
                      <th className="text-left py-2 px-3 text-gray-600 font-medium">Tip</th>
                      <th className="text-left py-2 px-3 text-gray-600 font-medium">Alt Tip</th>
                      <th className="text-right py-2 px-3"></th>
                    </tr>
                  </thead>
                  <tbody>
                    {equipment.map((eq) => (
                      <tr key={eq._tempId} className="border-b border-gray-100 hover:bg-gray-50">
                        <td className="py-2 px-3 font-medium text-gray-900">{eq.name}</td>
                        <td className="py-2 px-3 text-gray-600">{EQUIPMENT_TYPE_LABELS[eq.type] || eq.type}</td>
                        <td className="py-2 px-3 text-gray-600">{eq.subtype}</td>
                        <td className="py-2 px-3 text-right">
                          <button
                            onClick={() => handleRemoveEquipment(eq._tempId)}
                            className="p-1 text-red-500 hover:bg-red-50 rounded transition-colors"
                          >
                            <Trash2 className="w-4 h-4" />
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}

            <div className="mt-4">
              <button
                onClick={() => setShowModal(true)}
                className="flex items-center gap-2 px-3 py-2 text-indigo-600 border border-indigo-300 rounded-lg hover:bg-indigo-50 transition-colors"
              >
                <Plus className="w-4 h-4" />
                Ekipman Ekle
              </button>
            </div>
          </Card>

          <div className="flex items-center justify-between">
            <button
              onClick={() => setStep(2)}
              className="flex items-center gap-2 px-4 py-2 text-gray-600 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
            >
              <ArrowLeft className="w-4 h-4" />
              Geri
            </button>
            <button
              onClick={handleCreate}
              disabled={creating}
              className="flex items-center gap-2 px-6 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors disabled:opacity-50"
            >
              {creating ? (
                <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white" />
              ) : (
                <Check className="w-4 h-4" />
              )}
              Proje Oluştur
            </button>
          </div>
        </>
      )}

      {/* Error */}
      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700">
          {error}
        </div>
      )}

      {/* Add Equipment Modal */}
      {showModal && (
        <AddEquipmentModal
          onAdd={handleAddEquipment}
          onClose={() => setShowModal(false)}
        />
      )}
    </div>
  );
};

export default FactoryWizard;
