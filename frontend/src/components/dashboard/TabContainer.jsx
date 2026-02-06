const TabContainer = ({ tabs, activeTab, onTabChange, children }) => {
  return (
    <div>
      {/* Tab navigation bar */}
      <div className="flex border-b border-slate-200 mb-6">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => onTabChange(tab.id)}
            className={`px-5 py-3 text-sm font-medium transition-colors relative ${
              activeTab === tab.id
                ? 'text-cyan-600 font-semibold'
                : 'text-slate-500 hover:text-slate-700'
            }`}
          >
            {tab.label}
            {activeTab === tab.id && (
              <span className="absolute bottom-0 left-0 right-0 h-0.5 bg-cyan-600" />
            )}
          </button>
        ))}
      </div>

      {/* Tab content — all rendered, inactive hidden to preserve state */}
      {Array.isArray(children)
        ? children.map((child) => {
            if (!child) return null;
            const tabId = child.props?.['data-tab'] || child.key;
            return (
              <div key={tabId} className={tabId !== activeTab ? 'hidden' : 'animate-fade-in'}>
                {child}
              </div>
            );
          })
        : children}
    </div>
  );
};

export default TabContainer;
