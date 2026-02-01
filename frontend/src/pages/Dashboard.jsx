import { Link } from 'react-router-dom';
import { Wind, Flame, Snowflake, Droplets, ArrowRight, Factory } from 'lucide-react';

const equipmentCards = [
  {
    type: 'compressor',
    name: 'Kompresör',
    description: 'Hava ve gaz kompresörlerinin ekserji analizi',
    subtypes: 4,
    icon: Wind,
    color: 'text-blue-600',
    bg: 'bg-blue-50',
    border: 'border-blue-200',
  },
  {
    type: 'boiler',
    name: 'Kazan',
    description: 'Buhar ve sicak su kazanlarinin ekserji analizi',
    subtypes: 3,
    icon: Flame,
    color: 'text-orange-600',
    bg: 'bg-orange-50',
    border: 'border-orange-200',
  },
  {
    type: 'chiller',
    name: 'Chiller',
    description: 'Sogutma sistemlerinin ekserji analizi',
    subtypes: 3,
    icon: Snowflake,
    color: 'text-cyan-600',
    bg: 'bg-cyan-50',
    border: 'border-cyan-200',
  },
  {
    type: 'pump',
    name: 'Pompa',
    description: 'Pompa sistemlerinin ekserji analizi',
    subtypes: 3,
    icon: Droplets,
    color: 'text-emerald-600',
    bg: 'bg-emerald-50',
    border: 'border-emerald-200',
  },
];

const Dashboard = () => {
  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold text-gray-900">Dashboard</h2>
        <p className="text-gray-600 mt-1">
          Ekipman secin ve ekserji analizine baslayin
        </p>
      </div>

      {/* Equipment Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {equipmentCards.map((eq) => (
          <Link
            key={eq.type}
            to={`/equipment/${eq.type}`}
            className={`group bg-white rounded-xl border ${eq.border} p-6 hover:shadow-lg transition-all`}
          >
            <div className="flex items-start justify-between">
              <div className={`w-12 h-12 ${eq.bg} rounded-lg flex items-center justify-center`}>
                <eq.icon className={`w-6 h-6 ${eq.color}`} />
              </div>
              <ArrowRight className="w-5 h-5 text-gray-300 group-hover:text-gray-500 transition-colors" />
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mt-4">{eq.name}</h3>
            <p className="text-sm text-gray-600 mt-1">{eq.description}</p>
            <p className="text-xs text-gray-400 mt-3">{eq.subtypes} tip desteklenir</p>
          </Link>
        ))}
      </div>

      {/* Factory Analysis Promo */}
      <div className="bg-gradient-to-r from-primary-50 to-blue-50 rounded-xl border border-primary-200 p-6">
        <div className="flex items-start gap-4">
          <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center">
            <Factory className="w-6 h-6 text-primary-600" />
          </div>
          <div className="flex-1">
            <h3 className="text-lg font-semibold text-gray-900">Fabrika Analizi</h3>
            <p className="text-sm text-gray-600 mt-1">
              Tum fabrika ekipmanlarinizi tek bir projede analiz edin ve toplam ekserji performansini gorun.
            </p>
            <Link
              to="/factory"
              className="inline-flex items-center gap-1 mt-3 text-sm font-medium text-primary-600 hover:text-primary-700"
            >
              Yeni proje olustur
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
