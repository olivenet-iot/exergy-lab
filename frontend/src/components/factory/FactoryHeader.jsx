import { ArrowLeft, Factory, Plus, RefreshCw } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

const SECTOR_LABELS = {
  food: 'Gida',
  cement: 'Cimento',
  textile: 'Tekstil',
  paper: 'Kagit',
  metal: 'Metal',
  automotive: 'Otomotiv',
  chemical: 'Kimya',
};

const FactoryHeader = ({ project, onRefreshAnalysis, onAddEquipment, isAnalyzing }) => {
  const navigate = useNavigate();
  const hasEquipment = (project.equipment?.length || 0) > 0;

  return (
    <div className="flex items-center justify-between">
      <div className="flex items-center gap-3">
        <button
          onClick={() => navigate('/factory')}
          className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
        >
          <ArrowLeft className="w-5 h-5 text-gray-600" />
        </button>
        <Factory className="w-8 h-8 text-cyan-600" />
        <div>
          <div className="flex items-center gap-2">
            <h2 className="text-2xl font-bold text-gray-900">{project.name}</h2>
            {project.sector && (
              <span className="px-2 py-0.5 rounded text-xs font-medium bg-slate-100 text-slate-600">
                {SECTOR_LABELS[project.sector] || project.sector}
              </span>
            )}
          </div>
          <p className="text-gray-500 text-sm mt-0.5">
            {project.equipment_count || project.equipment?.length || 0} ekipman
          </p>
        </div>
      </div>
      <div className="flex items-center gap-2">
        <button
          onClick={onAddEquipment}
          className="flex items-center gap-2 px-4 py-2 border border-cyan-300 text-cyan-700 rounded-lg hover:bg-cyan-50 transition-colors"
        >
          <Plus className="w-4 h-4" />
          Ekipman Ekle
        </button>
        <button
          onClick={onRefreshAnalysis}
          disabled={isAnalyzing || !hasEquipment}
          className="flex items-center gap-2 px-4 py-2 bg-cyan-600 text-white rounded-lg hover:bg-cyan-700 transition-colors disabled:opacity-50"
        >
          {isAnalyzing ? (
            <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white" />
          ) : (
            <RefreshCw className="w-4 h-4" />
          )}
          Analizi Guncelle
        </button>
      </div>
    </div>
  );
};

export default FactoryHeader;
