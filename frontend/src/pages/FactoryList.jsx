import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Factory, Plus, Calendar, Settings } from 'lucide-react';
import { getFactoryProjects } from '../services/factoryApi';
import Card from '../components/common/Card';

const SECTOR_LABELS = {
  textile: 'Tekstil',
  food: 'Gıda',
  chemical: 'Kimya',
  metal: 'Metal',
  cement: 'Çimento',
  paper: 'Kağıt',
  automotive: 'Otomotiv',
};

const FactoryList = () => {
  const navigate = useNavigate();
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const data = await getFactoryProjects();
        setProjects(data.projects || []);
      } catch {
        setProjects([]);
      } finally {
        setLoading(false);
      }
    };
    fetchProjects();
  }, []);

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <Factory className="w-8 h-8 text-indigo-600" />
          <div>
            <h2 className="text-2xl font-bold text-gray-900">Fabrika Projeleri</h2>
            <p className="text-gray-600 mt-1">Fabrika seviyesi exergy analizi projeleri</p>
          </div>
        </div>
        <button
          onClick={() => navigate('/factory/new')}
          className="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors"
        >
          <Plus className="w-4 h-4" />
          Yeni Proje
        </button>
      </div>

      {/* Loading */}
      {loading && (
        <div className="flex items-center justify-center py-12">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600" />
        </div>
      )}

      {/* Empty state */}
      {!loading && projects.length === 0 && (
        <Card>
          <div className="flex flex-col items-center justify-center py-12 text-center">
            <Factory className="w-16 h-16 text-gray-300 mb-4" />
            <h3 className="text-lg font-medium text-gray-900">Henüz proje yok</h3>
            <p className="text-gray-500 mt-2">Yeni bir fabrika projesi oluşturarak başlayabilirsiniz.</p>
            <button
              onClick={() => navigate('/factory/new')}
              className="mt-4 flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors"
            >
              <Plus className="w-4 h-4" />
              Yeni Proje Oluştur
            </button>
          </div>
        </Card>
      )}

      {/* Project cards */}
      {!loading && projects.length > 0 && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {projects.map((project) => (
            <div
              key={project.id}
              onClick={() => navigate(`/factory/${project.id}`)}
              className="bg-white rounded-xl border border-gray-200 p-6 hover:border-indigo-300 hover:shadow-md transition-all cursor-pointer"
            >
              <div className="flex items-start justify-between">
                <div>
                  <h3 className="text-lg font-semibold text-gray-900">{project.name}</h3>
                  {project.sector && (
                    <span className="inline-block mt-1 px-2 py-0.5 text-xs font-medium bg-indigo-100 text-indigo-700 rounded">
                      {SECTOR_LABELS[project.sector] || project.sector}
                    </span>
                  )}
                </div>
                <Settings className="w-5 h-5 text-gray-400" />
              </div>

              <div className="mt-4 flex items-center gap-4 text-sm text-gray-500">
                <div className="flex items-center gap-1">
                  <Factory className="w-4 h-4" />
                  <span>{project.equipment_count || 0} ekipman</span>
                </div>
                {project.created_at && (
                  <div className="flex items-center gap-1">
                    <Calendar className="w-4 h-4" />
                    <span>{new Date(project.created_at).toLocaleDateString('tr-TR')}</span>
                  </div>
                )}
              </div>

              {project.description && (
                <p className="mt-3 text-sm text-gray-500 line-clamp-2">{project.description}</p>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default FactoryList;
