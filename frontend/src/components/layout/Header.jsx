import { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { getMe, logout } from '../../services/api';

const Header = () => {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const hasToken = !!localStorage.getItem('token');

  useEffect(() => {
    if (!hasToken) {
      setUser(null);
      return;
    }
    getMe()
      .then(setUser)
      .catch(() => {
        // Token invalid — clear it
        logout();
        setUser(null);
      });
  }, [hasToken]);

  const handleLogout = () => {
    logout();
    setUser(null);
    navigate('/login');
  };

  return (
    <header className="bg-white border-b border-gray-200 px-6 py-4">
      <div className="flex items-center justify-between max-w-7xl mx-auto">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-primary-600 rounded-lg flex items-center justify-center">
            <span className="text-white font-bold">Ex</span>
          </div>
          <div>
            <h1 className="text-xl font-bold text-gray-900">ExergyLab</h1>
            <p className="text-sm text-gray-500">Termodinamik Performans Analizi</p>
          </div>
        </div>

        <div className="flex items-center gap-4">
          {user ? (
            <>
              <span className="text-sm text-gray-700">
                {user.full_name || user.email}
              </span>
              <button
                onClick={handleLogout}
                className="text-sm text-gray-500 hover:text-gray-700 font-medium"
              >
                Cikis Yap
              </button>
            </>
          ) : (
            <Link
              to="/login"
              className="text-sm text-primary-600 hover:text-primary-700 font-medium"
            >
              Giris Yap
            </Link>
          )}
        </div>
      </div>
    </header>
  );
};

export default Header;
