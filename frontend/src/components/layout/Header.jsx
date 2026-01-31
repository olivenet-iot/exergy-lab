const Header = () => {
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
      </div>
    </header>
  );
};

export default Header;
