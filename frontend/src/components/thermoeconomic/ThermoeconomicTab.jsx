import { useState } from 'react';
import { TrendingUp, RefreshCw, AlertTriangle, ChevronDown, ChevronUp } from 'lucide-react';
import Card from '../common/Card';
import Plot from 'react-plotly.js';

const STRATEGY_COLORS = {
  invest: '#ef4444',
  parametric: '#f59e0b',
  structural: '#8b5cf6',
  downsize: '#3b82f6',
  maintain: '#22c55e',
};

const PRIORITY_COLORS = {
  high: '#ef4444',
  medium: '#f59e0b',
  low: '#22c55e',
};

/* ---------- Metric Cards ---------- */
const MetricCards = ({ data }) => {
  const cards = [
    { label: 'Toplam Tasarruf', value: `${(data.total_savings_annual_eur || 0).toLocaleString('tr-TR', { maximumFractionDigits: 0 })} EUR/yıl`, color: 'text-green-700' },
    { label: 'Tahmini Yatırım', value: `${(data.total_estimated_investment_eur || 0).toLocaleString('tr-TR', { maximumFractionDigits: 0 })} EUR`, color: 'text-blue-700' },
    { label: 'Geri Ödeme', value: `${(data.factory_payback_years || 0).toFixed(1)} yıl`, color: 'text-amber-700' },
    { label: 'Fabrika f-faktor', value: (data.factory_f_factor || 0).toFixed(2), color: 'text-teal-700' },
  ];

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
      {cards.map((c, i) => (
        <div key={i} className="bg-white border rounded-lg p-3 text-center">
          <div className={`text-lg font-bold ${c.color}`}>{c.value}</div>
          <div className="text-xs text-gray-500 mt-1">{c.label}</div>
        </div>
      ))}
    </div>
  );
};

/* ---------- Strategy Distribution ---------- */
const StrategyBadges = ({ distribution }) => {
  if (!distribution) return null;
  return (
    <div className="flex flex-wrap gap-2 mt-2">
      {Object.entries(distribution).map(([strat, count]) => (
        <span
          key={strat}
          className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium text-white"
          style={{ backgroundColor: STRATEGY_COLORS[strat] || '#9ca3af' }}
        >
          {strat}: {count}
        </span>
      ))}
    </div>
  );
};

/* ---------- f-r Scatter ---------- */
const FRScatterChart = ({ scatterData }) => {
  if (!scatterData?.equipment_names?.length) return null;

  const zones = scatterData.zones || {};
  const shapes = Object.entries(zones).map(([key, zone]) => ({
    type: 'rect',
    x0: zone.f_range[0],
    x1: zone.f_range[1],
    y0: zone.r_range[0],
    y1: zone.r_range[1],
    fillcolor: STRATEGY_COLORS[key] || '#9ca3af',
    opacity: 0.08,
    line: { color: STRATEGY_COLORS[key] || '#9ca3af', width: 1, dash: 'dot' },
  }));

  return (
    <Plot
      data={[{
        x: scatterData.f_factors,
        y: scatterData.r_factors,
        mode: 'markers+text',
        type: 'scatter',
        text: scatterData.equipment_names,
        textposition: 'top center',
        textfont: { size: 9 },
        marker: {
          color: scatterData.colors,
          size: scatterData.sizes,
          line: { width: 1, color: '#fff' },
        },
        hovertemplate: '%{text}<br>f=%{x:.2f}, r=%{y:.2f}<extra></extra>',
      }]}
      layout={{
        xaxis: { title: 'f-faktor', range: [0, 1.05], dtick: 0.25 },
        yaxis: { title: 'r-faktor', range: [0, Math.max(1.5, ...(scatterData.r_factors || [1]))], dtick: 0.25 },
        shapes,
        margin: { t: 20, b: 50, l: 50, r: 20 },
        height: 320,
        showlegend: false,
      }}
      config={{ displayModeBar: false, responsive: true }}
      useResizeHandler
      className="w-full"
    />
  );
};

/* ---------- Savings Waterfall ---------- */
const SavingsWaterfallChart = ({ waterfallData }) => {
  if (!waterfallData?.equipment_names?.length) return null;

  const traces = [
    {
      x: waterfallData.equipment_names,
      y: waterfallData.savings_eur,
      type: 'bar',
      marker: { color: waterfallData.colors },
      hovertemplate: '%{x}: %{y:,.0f} EUR/yıl<extra></extra>',
      name: 'Tasarruf',
    },
    {
      x: waterfallData.equipment_names,
      y: waterfallData.cumulative_eur,
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: '#1f2937', width: 2, dash: 'dot' },
      marker: { size: 5, color: '#1f2937' },
      hovertemplate: 'Kumulatif: %{y:,.0f} EUR/yıl<extra></extra>',
      name: 'Kumulatif',
      yaxis: 'y',
    },
  ];

  return (
    <Plot
      data={traces}
      layout={{
        yaxis: { title: 'EUR/yıl' },
        margin: { t: 20, b: 80, l: 60, r: 20 },
        height: 280,
        showlegend: false,
        bargap: 0.3,
      }}
      config={{ displayModeBar: false, responsive: true }}
      useResizeHandler
      className="w-full"
    />
  );
};

/* ---------- Optimization Ranking ---------- */
const RankingItem = ({ item, rank }) => {
  const [open, setOpen] = useState(false);
  const rec = item._recommendation;

  return (
    <div className="border rounded-lg p-3 bg-white">
      <div className="flex items-center justify-between cursor-pointer" onClick={() => setOpen(!open)}>
        <div className="flex items-center gap-2">
          <span className="text-xs font-bold text-gray-400">#{rank}</span>
          <span className="font-medium text-sm">{item.equipment_name}</span>
          <span
            className="px-2 py-0.5 rounded-full text-xs font-medium text-white"
            style={{ backgroundColor: STRATEGY_COLORS[item.strategy] || '#9ca3af' }}
          >
            {item.strategy_label}
          </span>
          <span
            className="px-1.5 py-0.5 rounded text-xs font-medium"
            style={{ color: PRIORITY_COLORS[item.priority] || '#6b7280' }}
          >
            {item.priority}
          </span>
        </div>
        <div className="flex items-center gap-3 text-xs text-gray-600">
          <span>{(item.C_savings_annual_eur || 0).toLocaleString('tr-TR', { maximumFractionDigits: 0 })} EUR/yıl</span>
          <span>{item.simple_payback_years}y</span>
          {open ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
        </div>
      </div>
      {open && rec?.recommended_actions && (
        <ul className="mt-2 pl-6 text-xs text-gray-600 list-disc space-y-1">
          {rec.recommended_actions.map((a, i) => <li key={i}>{a}</li>)}
        </ul>
      )}
    </div>
  );
};

const OptimizationRanking = ({ ranking, recommendations }) => {
  if (!ranking?.length) return <p className="text-sm text-gray-500 text-center py-4">Aksiyon gerektiren ekipman yok</p>;

  // Merge recommended_actions from full recommendations
  const recMap = {};
  (recommendations || []).forEach(r => { recMap[r.equipment_id] = r; });
  const enriched = ranking.map(r => ({ ...r, _recommendation: recMap[r.equipment_id] || {} }));

  return (
    <div className="space-y-2">
      {enriched.map((item, i) => (
        <RankingItem key={item.equipment_id} item={item} rank={i + 1} />
      ))}
    </div>
  );
};

/* ---------- Main Tab ---------- */
const ThermoeconomicTab = ({ thermoData, onRerun, isLoading }) => {
  if (!thermoData?.is_valid) {
    const msg = thermoData?.error_message || 'Termoekonomik optimizasyon için yeterli veri yok';
    return (
      <Card title="Termoekonomik Optimizasyon">
        <div className="text-center py-8">
          <TrendingUp className="w-10 h-10 text-gray-300 mx-auto mb-3" />
          <p className="text-gray-500 text-sm">{msg}</p>
        </div>
      </Card>
    );
  }

  return (
    <div className="space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-semibold text-gray-800 flex items-center gap-2">
          <TrendingUp className="w-5 h-5 text-teal-600" />
          Termoekonomik Optimizasyon
        </h3>
        {onRerun && (
          <button
            onClick={onRerun}
            disabled={isLoading}
            className="flex items-center gap-1 px-3 py-1 text-sm bg-teal-600 text-white rounded hover:bg-teal-700 transition-colors disabled:opacity-50"
          >
            {isLoading ? (
              <div className="animate-spin rounded-full h-3 w-3 border-b-2 border-white" />
            ) : (
              <RefreshCw className="w-3 h-3" />
            )}
            Yeniden Çalıştır
          </button>
        )}
      </div>

      {/* Metric Cards */}
      <MetricCards data={thermoData} />
      <StrategyBadges distribution={thermoData.strategy_distribution} />

      {/* Charts Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <Card title="f-Faktör vs r-Faktör (Strateji Haritası)">
          <FRScatterChart scatterData={thermoData.f_r_scatter_data} />
        </Card>
        <Card title="Tasarruf Sırası (Waterfall)">
          <SavingsWaterfallChart waterfallData={thermoData.savings_waterfall_data} />
        </Card>
      </div>

      {/* Optimization Ranking */}
      <Card title="Optimizasyon Sıralaması (ROI)">
        <OptimizationRanking
          ranking={thermoData.cost_benefit_ranking}
          recommendations={thermoData.recommendations}
        />
      </Card>

      {/* Warnings */}
      {thermoData.warnings?.length > 0 && (
        <div className="bg-amber-50 border border-amber-200 rounded-lg p-3">
          <div className="flex items-center gap-2 mb-1">
            <AlertTriangle className="w-4 h-4 text-amber-600" />
            <span className="text-sm font-medium text-amber-800">Uyarılar</span>
          </div>
          <ul className="text-xs text-amber-700 space-y-1">
            {thermoData.warnings.map((w, i) => (
              <li key={i}>{w}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ThermoeconomicTab;
