const PriorityBadge = ({ priority }) => {
  const styles = {
    high: 'bg-red-100 text-red-700',
    medium: 'bg-amber-100 text-amber-700',
    low: 'bg-gray-100 text-gray-700',
  };

  const labels = {
    high: 'Yuksek Oncelik',
    medium: 'Orta Oncelik',
    low: 'Dusuk Oncelik',
  };

  return (
    <span className={`px-2 py-0.5 rounded text-xs font-medium ${styles[priority] || ''}`}>
      {labels[priority] || priority}
    </span>
  );
};

const SolutionsList = ({ solutions }) => {
  if (!solutions || solutions.length === 0) return null;

  return (
    <div className="space-y-4">
      <h3 className="text-lg font-semibold text-gray-900">Iyilestirme Onerileri</h3>

      {solutions.map((solution) => (
        <div
          key={solution.id}
          className="bg-white border border-gray-200 rounded-xl p-4 hover:shadow-md transition-shadow"
        >
          <div className="flex items-start justify-between">
            <div>
              <div className="flex items-center gap-2">
                <h4 className="font-medium text-gray-900">{solution?.title ?? '—'}</h4>
                <PriorityBadge priority={solution?.priority} />
              </div>
              <p className="text-sm text-gray-600 mt-1">{solution?.description ?? '—'}</p>
            </div>
          </div>

          <div className="mt-4 grid grid-cols-3 gap-4 text-sm">
            <div>
              <span className="text-gray-500">Tasarruf Potansiyeli</span>
              <p className="font-semibold text-green-600">{solution?.potential_savings_percent ?? '—'}%</p>
            </div>
            <div>
              <span className="text-gray-500">Tahmini Yatirim</span>
              <p className="font-semibold">{solution?.estimated_investment_eur ?? '—'}</p>
            </div>
            <div>
              <span className="text-gray-500">Geri Odeme</span>
              <p className="font-semibold">{solution?.estimated_roi_years ?? '—'} yil</p>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default SolutionsList;
