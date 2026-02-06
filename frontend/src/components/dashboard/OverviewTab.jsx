import { Sparkles } from 'lucide-react';
import RadarBenchmark from '../results/RadarBenchmark';
import Card from '../common/Card';
import { formatNumber } from '../../utils/formatters';

const OverviewTab = ({ result, interpretation, aiLoading, onSwitchToAI }) => {
  if (!result) return null;

  const { metrics = {}, radar_data } = result;
  const hasAvUn = metrics.exergy_destroyed_avoidable_kW != null;

  return (
    <div className="space-y-6">
      {/* Two-column grid: Radar + AV/UN */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Left: Radar */}
        <div>
          {radar_data ? (
            <RadarBenchmark radarData={radar_data} />
          ) : (
            <Card>
              <div className="h-64 flex items-center justify-center text-slate-400">
                Radar benchmark verisi mevcut değil.
              </div>
            </Card>
          )}
        </div>

        {/* Right: AV/UN bar + Grade badge */}
        <div className="space-y-6">
          {hasAvUn && (
            <Card title="Yıkım Ayrıştırması (AV/UN)">
              <div className="space-y-3">
                <div className="flex items-center justify-between text-sm mb-1">
                  <span className="text-gray-600">Önlenebilir (AV)</span>
                  <span className="font-mono font-semibold text-red-600">
                    {formatNumber(metrics.exergy_destroyed_avoidable_kW)} kW
                  </span>
                </div>
                <div className="flex items-center justify-between text-sm mb-1">
                  <span className="text-gray-600">Önlenemez (UN)</span>
                  <span className="font-mono font-semibold text-gray-500">
                    {formatNumber(metrics.exergy_destroyed_unavoidable_kW)} kW
                  </span>
                </div>
                {/* Stacked horizontal bar */}
                <div className="w-full h-6 rounded-full overflow-hidden flex bg-gray-200">
                  {metrics.avoidable_ratio_pct > 0 && (
                    <div
                      className="h-full bg-red-500 flex items-center justify-center text-xs text-white font-semibold"
                      style={{ width: `${Math.max(metrics.avoidable_ratio_pct, 8)}%` }}
                    >
                      {formatNumber(metrics.avoidable_ratio_pct, 1)}%
                    </div>
                  )}
                  {(100 - (metrics.avoidable_ratio_pct || 0)) > 0 && (
                    <div
                      className="h-full bg-gray-400 flex items-center justify-center text-xs text-white font-semibold"
                      style={{ width: `${Math.max(100 - (metrics.avoidable_ratio_pct || 0), 8)}%` }}
                    >
                      {formatNumber(100 - (metrics.avoidable_ratio_pct || 0), 1)}%
                    </div>
                  )}
                </div>
                <div className="flex items-center gap-4 text-xs text-gray-500 mt-1">
                  <span className="flex items-center gap-1">
                    <span className="w-3 h-3 rounded-full bg-red-500 inline-block"></span>
                    Önlenebilir — iyileştirme potansiyeli
                  </span>
                  <span className="flex items-center gap-1">
                    <span className="w-3 h-3 rounded-full bg-gray-400 inline-block"></span>
                    Önlenemez — fiziksel sınır
                  </span>
                </div>
              </div>
            </Card>
          )}

          {/* Quick metrics summary */}
          <Card title="Temel Metrikler">
            <div className="space-y-3">
              <div className="flex justify-between items-center">
                <span className="text-gray-600 text-sm">Exergy Girişi</span>
                <span className="font-mono font-semibold">{formatNumber(metrics.exergy_input_kW)} kW</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-gray-600 text-sm">Faydalı Exergy</span>
                <span className="font-mono font-semibold text-green-600">{formatNumber(metrics.exergy_output_kW)} kW</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-gray-600 text-sm">Exergy Yıkımı</span>
                <span className="font-mono font-semibold text-red-600">{formatNumber(metrics.exergy_destroyed_kW)} kW</span>
              </div>
            </div>
          </Card>
        </div>
      </div>

      {/* AI Summary excerpt */}
      {aiLoading && (
        <Card>
          <div className="flex items-center gap-3 py-4 justify-center">
            <Sparkles className="w-5 h-5 text-purple-500 animate-pulse" />
            <span className="text-gray-600">AI yorumu hazırlanıyor...</span>
          </div>
        </Card>
      )}

      {interpretation?.summary && !aiLoading && (
        <Card>
          <div className="flex items-start gap-3">
            <Sparkles className="w-5 h-5 text-purple-500 mt-0.5 shrink-0" />
            <div>
              <p className="text-gray-700 leading-relaxed">
                {interpretation.summary}
              </p>
              {interpretation.key_insights?.length > 0 && (
                <ul className="mt-2 space-y-1">
                  {interpretation.key_insights.slice(0, 3).map((insight, i) => (
                    <li key={i} className="text-sm text-gray-600 flex items-start gap-1.5">
                      <span className="text-amber-500 mt-0.5">&#9679;</span>
                      {insight}
                    </li>
                  ))}
                </ul>
              )}
              <button
                onClick={() => onSwitchToAI?.()}
                className="text-sm text-cyan-600 hover:text-cyan-700 mt-2 font-medium"
              >
                Detayli AI yorumunu oku &rarr;
              </button>
            </div>
          </div>
        </Card>
      )}
    </div>
  );
};

export default OverviewTab;
