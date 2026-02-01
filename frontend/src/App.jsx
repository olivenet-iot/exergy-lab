import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/layout/Layout';
import Dashboard from './pages/Dashboard';
import EquipmentAnalysis from './pages/EquipmentAnalysis';

const FactoryPlaceholder = () => (
  <div className="flex flex-col items-center justify-center py-24 text-center">
    <h2 className="text-2xl font-bold text-gray-900">Fabrika Analizi</h2>
    <p className="text-gray-500 mt-2">Bu özellik yakında kullanıma sunulacaktır.</p>
  </div>
);

const ReportsPlaceholder = () => (
  <div className="flex flex-col items-center justify-center py-24 text-center">
    <h2 className="text-2xl font-bold text-gray-900">Raporlar</h2>
    <p className="text-gray-500 mt-2">Bu özellik yakında kullanıma sunulacaktır.</p>
  </div>
);

function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/equipment/:equipmentType" element={<EquipmentAnalysis />} />
          <Route path="/factory" element={<FactoryPlaceholder />} />
          <Route path="/reports" element={<ReportsPlaceholder />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

export default App;
