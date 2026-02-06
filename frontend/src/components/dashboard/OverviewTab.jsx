import RadarBenchmark from '../results/RadarBenchmark';
import AIInsightCard from '../results/AIInsightCard';
import DestructionBreakdown from '../results/DestructionBreakdown';
import ExergoeconomicSummary from '../results/ExergoeconomicSummary';
import Card from '../common/Card';

const OverviewTab = ({ result, interpretation, aiLoading, onSwitchToAI }) => {
  if (!result) return null;

  const { metrics = {}, radar_data } = result;

  return (
    <div className="space-y-6">
      {/* AI Insight Card (top, full width) */}
      <AIInsightCard
        summary={interpretation?.summary}
        topRecommendation={interpretation?.recommendations?.[0]}
        onViewDetails={onSwitchToAI}
        loading={aiLoading}
      />

      {/* Two-column: Radar (left) + Destruction Breakdown (right) */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
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

        <div>
          <DestructionBreakdown
            avoidableKW={metrics.exergy_destroyed_avoidable_kW}
            unavoidableKW={metrics.exergy_destroyed_unavoidable_kW}
            avoidableRatio={metrics.avoidable_ratio_pct}
            totalDestruction={metrics.exergy_destroyed_kW}
            destructionRatio={
              metrics.exergy_input_kW
                ? (metrics.exergy_destroyed_kW / metrics.exergy_input_kW) * 100
                : null
            }
          />
        </div>
      </div>

      {/* Exergoeconomic Summary (full width, conditional) */}
      <ExergoeconomicSummary
        fFactor={metrics.exergoeconomic_f_factor}
        rFactor={metrics.exergoeconomic_r_factor}
        zDot={metrics.exergoeconomic_Z_dot_eur_h}
        cDotDestruction={metrics.exergoeconomic_C_dot_destruction_eur_h}
      />
    </div>
  );
};

export default OverviewTab;
