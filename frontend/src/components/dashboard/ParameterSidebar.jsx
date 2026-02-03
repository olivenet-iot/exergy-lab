import { ChevronLeft, ChevronRight, RotateCcw } from 'lucide-react';

const ParameterSidebar = ({
  equipmentType,
  equipmentName,
  equipmentIcon: Icon,
  equipmentColor,
  subtype,
  children,
  isCollapsed,
  onToggleCollapse,
  onReanalyze,
  loading,
}) => {
  return (
    <div
      className={`sidebar-transition bg-slate-900 border-r border-slate-700 flex flex-col ${
        isCollapsed ? 'w-14' : 'w-72'
      }`}
    >
      {isCollapsed ? (
        /* Collapsed state */
        <div className="flex flex-col items-center py-4 gap-3">
          <button
            onClick={onToggleCollapse}
            className="p-2 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white transition-colors"
            title="Parametreleri göster"
          >
            <ChevronRight className="w-5 h-5" />
          </button>
          {Icon && <Icon className={`w-5 h-5 ${equipmentColor || 'text-slate-400'}`} />}
        </div>
      ) : (
        /* Expanded state */
        <>
          {/* Header */}
          <div className="px-4 py-4 border-b border-slate-700">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                {Icon && <Icon className={`w-5 h-5 ${equipmentColor || 'text-slate-400'}`} />}
                <div>
                  <h3 className="text-sm font-semibold text-white">{equipmentName}</h3>
                  {subtype && (
                    <p className="text-xs text-slate-400">{subtype}</p>
                  )}
                </div>
              </div>
              <button
                onClick={onToggleCollapse}
                className="p-1.5 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white transition-colors"
                title="Gizle"
              >
                <ChevronLeft className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Scrollable form area with dark theme wrapper */}
          <div className="flex-1 overflow-y-auto px-4 py-4 custom-scrollbar dark-sidebar-form">
            {children}
          </div>

          {/* Footer buttons */}
          <div className="px-4 py-3 border-t border-slate-700 space-y-2">
            <button
              onClick={onReanalyze}
              disabled={loading}
              className="w-full py-2 px-4 bg-cyan-600 hover:bg-cyan-700 disabled:opacity-50 text-white text-sm font-medium rounded-lg transition-colors flex items-center justify-center gap-2"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              {loading ? 'Hesaplanıyor...' : 'Tekrar Analiz'}
            </button>
          </div>
        </>
      )}
    </div>
  );
};

export default ParameterSidebar;
