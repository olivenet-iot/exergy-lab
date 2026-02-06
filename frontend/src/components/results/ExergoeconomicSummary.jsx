import { formatNumber } from '../../utils/formatters';

const ExergoeconomicSummary = ({ fFactor, rFactor, zDot, cDotDestruction }) => {
  if (fFactor == null && rFactor == null && zDot == null && cDotDestruction == null) {
    return null;
  }

  const fPct = fFactor != null ? (fFactor * 100) : null;
  const interpretation = fFactor != null
    ? fFactor > 0.5
      ? 'Yatirim maliyeti baskin — ekipman maliyeti yikim maliyetinden yuksek.'
      : 'Yikim maliyeti baskin — exergy yikim maliyeti yatirimdan yuksek, verim iyilestirmesi oncelikli.'
    : null;

  const metrics = [
    {
      label: 'f Faktoru',
      value: fFactor != null ? formatNumber(fFactor, 3) : '—',
      sub: fPct != null ? `%${formatNumber(fPct, 1)}` : null,
      barPct: fPct,
      barColor: 'bg-blue-500',
    },
    {
      label: 'r Faktoru',
      value: rFactor != null ? formatNumber(rFactor, 3) : '—',
      sub: null,
      barPct: rFactor != null ? Math.min(rFactor * 100, 100) : null,
      barColor: 'bg-violet-500',
    },
    {
      label: 'Z (EUR/h)',
      value: zDot != null ? formatNumber(zDot, 2) : '—',
      sub: 'Yatirim akisi',
      barPct: null,
      barColor: null,
    },
    {
      label: 'C_D (EUR/h)',
      value: cDotDestruction != null ? formatNumber(cDotDestruction, 2) : '—',
      sub: 'Yikim akisi',
      barPct: null,
      barColor: null,
    },
  ];

  return (
    <div className="bg-white rounded-xl border border-gray-200 p-6">
      <h3 className="text-base font-semibold text-gray-900 mb-4">Exergoekonomik Ozet</h3>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {metrics.map((m) => (
          <div key={m.label} className="space-y-1">
            <span className="text-xs text-gray-500">{m.label}</span>
            <p className="text-lg font-bold font-mono text-gray-900">{m.value}</p>
            {m.barPct != null && (
              <div className="w-full h-1.5 bg-gray-100 rounded-full overflow-hidden">
                <div
                  className={`h-full rounded-full ${m.barColor}`}
                  style={{ width: `${Math.max(m.barPct, 2)}%` }}
                />
              </div>
            )}
            {m.sub && <span className="text-xs text-gray-400">{m.sub}</span>}
          </div>
        ))}
      </div>

      {interpretation && (
        <p className="mt-4 text-sm text-gray-600 bg-slate-50 rounded-lg p-3">
          {interpretation}
        </p>
      )}
    </div>
  );
};

export default ExergoeconomicSummary;
