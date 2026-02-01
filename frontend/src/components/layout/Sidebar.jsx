import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  Wind,
  Flame,
  Snowflake,
  Droplets,
  Factory,
  FolderOpen,
  ChevronDown,
} from 'lucide-react';

const equipmentLinks = [
  { to: '/equipment/compressor', label: 'Kompresör', icon: Wind },
  { to: '/equipment/boiler', label: 'Kazan', icon: Flame },
  { to: '/equipment/chiller', label: 'Chiller', icon: Snowflake },
  { to: '/equipment/pump', label: 'Pompa', icon: Droplets },
];

const factoryLinks = [
  { to: '/factory', label: 'Yeni Proje', icon: Factory },
  { to: '/reports', label: 'Raporlar', icon: FolderOpen },
];

const linkClass = ({ isActive }) =>
  `flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
    isActive
      ? 'bg-primary-50 text-primary-700'
      : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'
  }`;

const CollapsibleGroup = ({ title, children, defaultOpen = true }) => {
  const [open, setOpen] = useState(defaultOpen);

  return (
    <div>
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center justify-between w-full px-3 py-2 text-xs font-semibold text-gray-400 uppercase tracking-wider hover:text-gray-600"
      >
        {title}
        <ChevronDown
          className={`w-4 h-4 transition-transform ${open ? '' : '-rotate-90'}`}
        />
      </button>
      {open && <div className="space-y-1">{children}</div>}
    </div>
  );
};

const Sidebar = () => {
  return (
    <aside className="w-64 bg-white border-r border-gray-200 flex flex-col h-screen sticky top-0">
      {/* Logo */}
      <div className="px-5 py-5 border-b border-gray-200">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-primary-600 rounded-lg flex items-center justify-center">
            <span className="text-white font-bold">Ex</span>
          </div>
          <div>
            <h1 className="text-lg font-bold text-gray-900">ExergyLab</h1>
            <p className="text-xs text-gray-500">Termodinamik Performans</p>
          </div>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 px-3 py-4 space-y-6 overflow-y-auto">
        {/* Dashboard */}
        <div>
          <NavLink to="/" end className={linkClass}>
            <LayoutDashboard className="w-5 h-5" />
            Dashboard
          </NavLink>
        </div>

        {/* Equipment Analysis */}
        <CollapsibleGroup title="Ekipman Analizi">
          {equipmentLinks.map((link) => (
            <NavLink key={link.to} to={link.to} className={linkClass}>
              <link.icon className="w-5 h-5" />
              {link.label}
            </NavLink>
          ))}
        </CollapsibleGroup>

        {/* Factory Analysis */}
        <CollapsibleGroup title="Fabrika Analizi">
          {factoryLinks.map((link) => (
            <NavLink key={link.to} to={link.to} className={linkClass}>
              <link.icon className="w-5 h-5" />
              {link.label}
            </NavLink>
          ))}
        </CollapsibleGroup>
      </nav>

      {/* Footer */}
      <div className="px-5 py-4 border-t border-gray-200">
        <p className="text-xs text-gray-400">ExergyLab v0.1</p>
      </div>
    </aside>
  );
};

export default Sidebar;
