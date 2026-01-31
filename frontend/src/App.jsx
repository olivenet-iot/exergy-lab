import { useState } from 'react';
import Layout from './components/layout/Layout';
import CompressorTypeSelector from './components/forms/CompressorTypeSelector';
import ParameterForm from './components/forms/ParameterForm';
import ResultsPanel from './components/results/ResultsPanel';
import SolutionsList from './components/results/SolutionsList';
import AIInterpretation from './components/results/AIInterpretation';
import Card from './components/common/Card';
import LoadingSpinner from './components/common/Loading';
import { useCompressorTypes } from './hooks/useCompressorTypes';
import { useAnalysis } from './hooks/useAnalysis';

function App() {
  const { types, loading: typesLoading } = useCompressorTypes();
  const { result, solutions, loading, error, analyze, reset, interpretation, aiLoading } = useAnalysis();

  const [selectedType, setSelectedType] = useState(null);
  const [formValues, setFormValues] = useState({});

  const selectedTypeData = types?.find(t => t.id === selectedType);

  const handleTypeSelect = (typeId) => {
    setSelectedType(typeId);
    setFormValues({});
    reset();
  };

  const handleFormChange = (fieldId, value) => {
    setFormValues(prev => ({ ...prev, [fieldId]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    analyze(selectedType, formValues);
  };

  return (
    <Layout>
      <div className="space-y-8">
        {/* Title */}
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Kompresor Exergy Analizi</h2>
          <p className="text-gray-600 mt-1">
            Kompresor tipini secin ve parametreleri girin
          </p>
        </div>

        {/* Compressor Type Selection */}
        <Card title="1. Kompresor Tipi">
          {typesLoading ? (
            <div className="h-32 flex items-center justify-center">
              <LoadingSpinner />
            </div>
          ) : (
            <CompressorTypeSelector
              types={types}
              selected={selectedType}
              onSelect={handleTypeSelect}
            />
          )}
        </Card>

        {/* Parameter Form */}
        {selectedTypeData && (
          <Card title="2. Parametreler">
            <ParameterForm
              fields={selectedTypeData.fields}
              values={formValues}
              onChange={handleFormChange}
              onSubmit={handleSubmit}
              loading={loading}
            />
          </Card>
        )}

        {/* Error Message */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700">
            {error}
          </div>
        )}

        {/* Results */}
        {result && (
          <>
            <div className="border-t border-gray-200 pt-8">
              <h2 className="text-2xl font-bold text-gray-900 mb-6">Analiz Sonuclari</h2>
              <ResultsPanel data={result} />
            </div>

            <AIInterpretation interpretation={interpretation} loading={aiLoading} />

            {!interpretation && !aiLoading && solutions.length > 0 && (
              <SolutionsList solutions={solutions} />
            )}
          </>
        )}
      </div>
    </Layout>
  );
}

export default App;
