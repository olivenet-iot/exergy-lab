import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Wind, Flame, Snowflake, Droplets, Clock } from 'lucide-react';
import { getCompressorTypes, getEquipmentSubtypes } from '../services/api';
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

  // Fetch subtypes when equipment type changes
  useEffect(() => {
    setSubtypes([]);
    setSelectedSubtype(null);
    setFormValues({});
    reset();
    setSubtypesLoading(true);

    const fetchSubtypes = async () => {
      try {
        if (equipmentType === 'compressor') {
          const data = await getCompressorTypes();
          setSubtypes(data);
        } else {
          const data = await getEquipmentSubtypes(equipmentType);
          setSubtypes(
            (data.subtypes || []).map((s) => ({
              id: s.id || s.type,
              name: s.name || s.label || s.id,
              ...s,
            }))
          );
        }
      } catch {
        setSubtypes([]);
      } finally {
        setSubtypesLoading(false);
      }
    };

    fetchSubtypes();
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
    analyze(selectedSubtype, formValues);
  };

  const isCompressor = equipmentType === 'compressor';
  const selectedSubtypeData = subtypes?.find((t) => (t.id || t.type) === selectedSubtype);

  return (
    <div className="space-y-8">
      {/* Title */}
      <div className="flex items-center gap-3">
        <Icon className={`w-8 h-8 ${meta.color}`} />
        <div>
          <h2 className="text-2xl font-bold text-gray-900">{meta.name} Ekserji Analizi</h2>
          <p className="text-gray-600 mt-1">
            {isCompressor
              ? 'Kompresör tipini seçin ve parametreleri girin'
              : `${meta.name} tipini seçin`}
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

      {/* Compressor: full analysis flow */}
      {isCompressor && selectedSubtypeData && (
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
              {error}
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

      {/* Non-compressor: coming soon */}
      {!isCompressor && selectedSubtype && (
        <Card>
          <div className="flex flex-col items-center justify-center py-12 text-center">
            <Clock className="w-12 h-12 text-gray-300 mb-4" />
            <h3 className="text-lg font-semibold text-gray-700">Yakında...</h3>
            <p className="text-sm text-gray-500 mt-2 max-w-md">
              {meta.name} ekserji analiz motoru geliştirme aşamasındadır.
              Yakında bu ekipman tipi için de tam analiz yapabileceksiniz.
            </p>
          </div>
        </Card>
      )}
    </div>
  );
};

export default EquipmentAnalysis;
