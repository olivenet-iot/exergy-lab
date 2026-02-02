import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Wind, Flame, Snowflake, Droplets, ArrowLeftRight, Zap, Sun } from 'lucide-react';
import { getEquipmentConfig } from '../services/api';
import { useAnalysis } from '../hooks/useAnalysis';
import SubtypeSelector from '../components/equipment/SubtypeSelector';
import ParameterForm from '../components/forms/ParameterForm';
import ResultsPanel from '../components/results/ResultsPanel';
import SolutionsList from '../components/results/SolutionsList';
import AIInterpretation from '../components/results/AIInterpretation';
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

  // Fetch subtypes with field definitions when equipment type changes
  useEffect(() => {
    setSubtypes([]);
    setSelectedSubtype(null);
    setFormValues({});
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
    reset();
  };

  const handleFormChange = (fieldId, value) => {
    setFormValues((prev) => ({ ...prev, [fieldId]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    analyze(equipmentType, selectedSubtype, formValues);
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
            </>
          )}
        </>
      )}
    </div>
  );
};

export default EquipmentAnalysis;
