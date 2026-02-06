import { Flame, TrendingDown, EuroIcon } from 'lucide-react';
import GaugeChart from './GaugeChart';
import { getPerformanceHex, getGradeInfo } from '../../utils/performanceColors';
import { formatNumber, formatCurrency } from '../../utils/formatters';

const HeroScoreBanner = ({
  efficiency,
  grade,
  destructionKW,
  avoidableKW,
  unavoidableKW,
  annualLossEUR,
  avoidableRatio,
}) => {
  const gaugeColor = getPerformanceHex(efficiency ?? 0);
  const gradeInfo = getGradeInfo(grade);

  return (
    <div className="bg-white rounded-xl shadow-md border border-slate-100 p-6">
      <div className="flex flex-col md:flex-row items-center gap-6">
        {/* Left: Gauge + Grade */}
        <div className="flex flex-col items-center gap-2 min-w-[140px]">
          <div className="w-[140px] h-[80px]">
            <GaugeChart value={efficiency} color={gaugeColor} />
          </div>
          {grade && (
            <span className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-sm font-bold ${gradeInfo.colorClass}`}>
              {grade} — {gradeInfo.label}
            </span>
          )}
        </div>

        {/* Right: 3 KPI blocks */}
        <div className="flex-1 grid grid-cols-1 sm:grid-cols-3 gap-4 w-full">
          {/* Destruction */}
          <div className="bg-slate-50 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <Flame className="w-4 h-4 text-red-500" />
              <span className="text-xs font-medium text-slate-500 uppercase tracking-wider">Yikim</span>
            </div>
            <p className="text-xl font-bold font-mono text-red-600">
              {formatNumber(destructionKW)} <span className="text-sm font-normal text-slate-500">kW</span>
            </p>
            {avoidableKW != null && unavoidableKW != null && (
              <div className="mt-2 text-xs text-slate-500 space-y-0.5">
                <div className="flex justify-between">
                  <span>Onlenebilir</span>
                  <span className="font-mono text-red-500">{formatNumber(avoidableKW)} kW</span>
                </div>
                <div className="flex justify-between">
                  <span>Onlenemez</span>
                  <span className="font-mono text-slate-400">{formatNumber(unavoidableKW)} kW</span>
                </div>
              </div>
            )}
          </div>

          {/* Annual Loss */}
          <div className="bg-slate-50 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <EuroIcon className="w-4 h-4 text-amber-500" />
              <span className="text-xs font-medium text-slate-500 uppercase tracking-wider">Yillik Kayip</span>
            </div>
            <p className="text-xl font-bold font-mono text-amber-600">
              {formatCurrency(annualLossEUR)}
            </p>
            <p className="mt-2 text-xs text-slate-500">
              Yillik exergy kaybi maliyeti
            </p>
          </div>

          {/* Avoidable Ratio */}
          <div className="bg-slate-50 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <TrendingDown className="w-4 h-4 text-emerald-500" />
              <span className="text-xs font-medium text-slate-500 uppercase tracking-wider">Kacinilabilir</span>
            </div>
            <p className="text-xl font-bold font-mono text-emerald-600">
              {avoidableRatio != null ? `%${formatNumber(avoidableRatio)}` : '—'}
            </p>
            {avoidableKW != null && (
              <p className="mt-2 text-xs text-slate-500">
                {formatNumber(avoidableKW)} kW iyilestirme potansiyeli
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default HeroScoreBanner;
