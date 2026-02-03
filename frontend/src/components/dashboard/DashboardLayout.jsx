const DashboardLayout = ({ hasResult, sidebar, metricBar, children }) => {
  if (!hasResult) {
    return (
      <div className="max-w-2xl mx-auto py-8">
        {children}
      </div>
    );
  }

  return (
    <div className="-mx-8 -mt-8 flex h-[calc(100vh-0px)] overflow-hidden">
      {sidebar}
      <div className="flex-1 flex flex-col min-w-0">
        {metricBar}
        <div className="flex-1 overflow-y-auto px-6 py-4 custom-scrollbar">
          {children}
        </div>
      </div>
    </div>
  );
};

export default DashboardLayout;
