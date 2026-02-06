import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/layout/Layout';
import Dashboard from './pages/Dashboard';
import EquipmentAnalysis from './pages/EquipmentAnalysis';
import FactoryList from './pages/FactoryList';
import FactoryWizard from './pages/FactoryWizard';
import FactoryDashboard from './pages/FactoryDashboard';
import Login from './pages/Login';

const ReportsPlaceholder = () => (
  <div className="flex flex-col items-center justify-center py-24 text-center">
    <h2 className="text-2xl font-bold text-gray-900">Raporlar</h2>
    <p className="text-gray-500 mt-2">Bu özellik yakında kullanıma sunulacaktır.</p>
  </div>
);

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="*" element={
          <Layout>
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/equipment/:equipmentType" element={<EquipmentAnalysis />} />
              <Route path="/factory" element={<FactoryList />} />
              <Route path="/factory/new" element={<FactoryWizard />} />
              <Route path="/factory/:projectId" element={<FactoryDashboard />} />
              <Route path="/reports" element={<ReportsPlaceholder />} />
              <Route path="*" element={<Navigate to="/" replace />} />
            </Routes>
          </Layout>
        } />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
