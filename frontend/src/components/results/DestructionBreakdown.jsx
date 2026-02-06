import { formatNumber } from '../../utils/formatters';

const DestructionBreakdown = ({
  avoidableKW,
  unavoidableKW,
  avoidableRatio,
  totalDestruction,
  destructionRatio,
}) => {
  const hasData = avoidableKW != null && unavoidableKW != null;
  if (!hasData) return null;

  const avPct = avoidableRatio ?? 0;
  const unPct = 100 - avPct;

  return (
    <div className="bg-white rounded-xl border border-gray-200 p-6">
      <h3 className="text-base font-semibold text-gray-900 mb-4">Yikim Ayristirmasi (AV/UN)</h3>

      <div className="space-y-4">
        {/* Avoidable bar */}
        <div>
          <div className="flex items-center justify-between text-sm mb-1.5">
            <span className="text-gray-600 flex items-center gap-1.5">
              <span className="w-3 h-3 rounded-full bg-red-500 inline-block" />
              Onlenebilir (AV)
            </span>
            <span className="font-mono font-semibold text-red-600">
              {formatNumber(avoidableKW)} kW
            </span>
          </div>
          <div className="w-full h-3 bg-gray-100 rounded-full overflow-hidden">
            <div
              className="h-full bg-red-500 rounded-full transition-all duration-500"
              style={{ width: `${Math.max(avPct, 2)}%` }}
            />
          </div>
          <div className="text-right text-xs text-gray-500 mt-0.5 font-mono">%{formatNumber(avPct, 1)}</div>
        </div>

        {/* Unavoidable bar */}
        <div>
          <div className="flex items-center justify-between text-sm mb-1.5">
            <span className="text-gray-600 flex items-center gap-1.5">
              <span className="w-3 h-3 rounded-full bg-gray-400 inline-block" />
              Onlenemez (UN)
            </span>
            <span className="font-mono font-semibold text-gray-500">
              {formatNumber(unavoidableKW)} kW
            </span>
          </div>
          <div className="w-full h-3 bg-gray-100 rounded-full overflow-hidden">
            <div
              className="h-full bg-gray-400 rounded-full transition-all duration-500"
              style={{ width: `${Math.max(unPct, 2)}%` }}
            />
          </div>
          <div className="text-right text-xs text-gray-500 mt-0.5 font-mono">%{formatNumber(unPct, 1)}</div>
        </div>

        {/* Total */}
        {totalDestruction != null && (
          <div className="border-t border-gray-100 pt-3 mt-3">
            <div className="flex items-center justify-between text-sm">
              <span className="text-gray-700 font-medium">Toplam Yikim</span>
              <span className="font-mono font-bold text-gray-900">
                {formatNumber(totalDestruction)} kW
              </span>
            </div>
            {destructionRatio != null && (
              <div className="flex items-center justify-between text-xs text-gray-500 mt-1">
                <span>Girise oranla</span>
                <span className="font-mono">%{formatNumber(destructionRatio, 1)}</span>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default DestructionBreakdown;
