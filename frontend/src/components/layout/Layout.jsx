import Sidebar from './Sidebar';

const Layout = ({ children }) => {
  return (
    <div className="flex min-h-screen bg-gray-50">
      <Sidebar />
      <div className="flex-1 flex flex-col min-h-screen">
        <main className="flex-1 px-8 py-8 max-w-7xl w-full">
          {children}
        </main>
      </div>
    </div>
  );
};

export default Layout;
