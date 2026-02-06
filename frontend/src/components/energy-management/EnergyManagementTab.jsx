import { useState } from 'react';
import { Shield, RefreshCw, AlertTriangle, ChevronDown, ChevronUp } from 'lucide-react';
import Card from '../common/Card';
import Plot from 'react-plotly.js';

const CATEGORY_COLORS = {
  quick_win: '#22c55e',
  medium_term: '#f59e0b',
  strategic: '#8b5cf6',
  monitoring: '#3b82f6',
};

const PRIORITY_COLORS = {
  high: '#ef4444',
  medium: '#f59e0b',
  low: '#22c55e',
};

/* ---------- Maturity Score Bar ---------- */
const MaturityBar = ({ score, level, label }) => {
  const pct = Math.min(100, Math.max(0, score));
  const barColor =
    pct >= 90 ? '#22c55e' : pct >= 70 ? '#3b82f6' : pct >= 50 ? '#f59e0b' : pct >= 30 ? '#f97316' : '#ef4444';

  return (
    <div className="mb-6">
      <div className="flex items-center justify-between mb-2">
        <h3 className="text-lg font-semibold text-gray-800">ISO 50001 Olgunluk Skoru</h3>
        <span className="text-sm font-medium" style={{ color: barColor }}>{label}</span>
      </div>
      <div className="w-full bg-gray-200 rounded-full h-5 relative">
        <div
          className="h-5 rounded-full transition-all duration-500 flex items-center justify-end pr-2"
          style={{ width: `${pct}%`, backgroundColor: barColor, minWidth: '2rem' }}
        >
          <span className="text-xs font-bold text-white">{score}/100</span>
        </div>
      </div>
    </div>
  );
};

/* ---------- EnPI Summary Cards ---------- */
const EnPICards = ({ enpi }) => {
  if (!enpi) return null;
  const cards = [
    { label: 'Exergy Verimi', value: `${(enpi.exergy_efficiency_pct || 0).toFixed(1)}%`, color: 'text-green-700' },
    { label: 'SEC', value: (enpi.specific_exergy_consumption || 0).toFixed(2), color: 'text-blue-700' },
    { label: 'Yıkım Oranı', value: `${(enpi.exergy_destruction_ratio_pct || 0).toFixed(1)}%`, color: 'text-red-700' },
    { label: 'Kaçınılabilir', value: `${(enpi.avoidable_loss_ratio_pct || 0).toFixed(1)}%`, color: 'text-amber-700' },
    { label: 'Maliyet Yog.', value: (enpi.energy_cost_intensity_eur_kWh || 0).toFixed(4), color: 'text-teal-700' },
    { label: 'Isı Geri Kaz.', value: `${(enpi.heat_recovery_potential_pct || 0).toFixed(1)}%`, color: 'text-cyan-700' },
    { label: 'Entropi Yog.', value: (enpi.entropy_generation_intensity || 0).toFixed(3), color: 'text-purple-700' },
  ];

  return (
    <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-3 mb-6">
      {cards.map((c, i) => (
        <div key={i} className="bg-white border rounded-lg p-3 text-center">
          <div className={`text-lg font-bold ${c.color}`}>{c.value}</div>
          <div className="text-xs text-gray-500 mt-1">{c.label}</div>
        </div>
      ))}
    </div>
  );
};

/* ---------- Radar Charts ---------- */
const DualRadarCharts = ({ maturityRadar, enpiRadar }) => {
  const maturityTrace = maturityRadar ? {
    type: 'scatterpolar',
    r: [...(maturityRadar.values || []), (maturityRadar.values || [])[0]],
    theta: [...(maturityRadar.categories || []), (maturityRadar.categories || [])[0]],
    fill: 'toself',
    name: 'Olgunluk',
    fillcolor: 'rgba(59,130,246,0.2)',
    line: { color: '#3b82f6' },
  } : null;

  const enpiTrace = enpiRadar ? {
    type: 'scatterpolar',
    r: [...(enpiRadar.values || []), (enpiRadar.values || [])[0]],
    theta: [...(enpiRadar.categories || []), (enpiRadar.categories || [])[0]],
    fill: 'toself',
    name: 'EnPI',
    fillcolor: 'rgba(16,185,129,0.2)',
    line: { color: '#10b981' },
  } : null;

  const layout = {
    polar: { radialaxis: { visible: true, range: [0, 100] } },
    margin: { t: 30, b: 30, l: 60, r: 60 },
    height: 320,
    showlegend: false,
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
  };

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-6">
      {maturityTrace && (
        <div className="bg-white border rounded-lg p-3">
          <h4 className="text-sm font-semibold text-gray-700 mb-2 text-center">Olgunluk Radar</h4>
          <Plot data={[maturityTrace]} layout={layout} config={{ displayModeBar: false, responsive: true }} className="w-full" />
        </div>
      )}
      {enpiTrace && (
        <div className="bg-white border rounded-lg p-3">
          <h4 className="text-sm font-semibold text-gray-700 mb-2 text-center">EnPI Radar</h4>
          <Plot data={[enpiTrace]} layout={layout} config={{ displayModeBar: false, responsive: true }} className="w-full" />
        </div>
      )}
    </div>
  );
};

/* ---------- Gap Analysis ---------- */
const GapAnalysis = ({ dimensions }) => {
  const gaps = (dimensions || []).filter((d) => d.score < 70);
  if (gaps.length === 0) return null;

  return (
    <div className="mb-6">
      <h3 className="text-base font-semibold text-gray-800 mb-3">Bosluk Analizi</h3>
      <div className="space-y-3">
        {gaps.map((d) => (
          <div key={d.dimension} className="bg-amber-50 border border-amber-200 rounded-lg p-3">
            <div className="flex items-center justify-between mb-1">
              <span className="font-medium text-amber-800">
                <AlertTriangle className="w-4 h-4 inline mr-1" />
                {d.label} ({d.iso_clause})
              </span>
              <span className="text-sm font-bold text-amber-700">{d.score}/100</span>
            </div>
            {d.gaps && d.gaps.length > 0 && (
              <ul className="text-sm text-amber-700 mt-1 space-y-0.5">
                {d.gaps.map((g, i) => (
                  <li key={i} className="ml-4">→ {g}</li>
                ))}
              </ul>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

/* ---------- Action Plan ---------- */
const ActionPlan = ({ actions, summary }) => {
  const [expanded, setExpanded] = useState(true);
  if (!actions || actions.length === 0) return null;

  const grouped = {};
  for (const a of actions) {
    if (!grouped[a.category]) grouped[a.category] = [];
    grouped[a.category].push(a);
  }

  const categoryOrder = ['quick_win', 'medium_term', 'strategic', 'monitoring'];
  const categoryLabels = {
    quick_win: 'Hızlı Kazanım (0-3 ay)',
    medium_term: 'Orta Vadeli (3-12 ay)',
    strategic: 'Stratejik (1-3 yıl)',
    monitoring: 'İzleme (Sürekli)',
  };

  return (
    <div>
      <div
        className="flex items-center justify-between cursor-pointer mb-3"
        onClick={() => setExpanded(!expanded)}
      >
        <h3 className="text-base font-semibold text-gray-800">
          Eylem Plani ({actions.length} aksiyon)
        </h3>
        {expanded ? <ChevronUp className="w-5 h-5 text-gray-500" /> : <ChevronDown className="w-5 h-5 text-gray-500" />}
      </div>

      {expanded && categoryOrder.map((cat) => {
        const items = grouped[cat];
        if (!items || items.length === 0) return null;
        return (
          <div key={cat} className="mb-4">
            <div className="flex items-center gap-2 mb-2">
              <span
                className="w-3 h-3 rounded-full"
                style={{ backgroundColor: CATEGORY_COLORS[cat] }}
              />
              <span className="text-sm font-semibold text-gray-700">{categoryLabels[cat]}</span>
            </div>
            <div className="space-y-2 ml-5">
              {items.map((a) => (
                <div key={a.id} className="flex items-start gap-3 bg-white border rounded-lg p-3 text-sm">
                  <span className="font-mono text-xs text-gray-400 mt-0.5">{a.id}</span>
                  <div className="flex-1">
                    <div className="flex items-center gap-2">
                      {a.equipment_name && (
                        <span className="text-xs px-1.5 py-0.5 bg-gray-100 rounded text-gray-600">
                          {a.equipment_name}
                        </span>
                      )}
                      <span
                        className="text-xs px-1.5 py-0.5 rounded text-white"
                        style={{ backgroundColor: PRIORITY_COLORS[a.priority] || '#9ca3af' }}
                      >
                        {a.priority}
                      </span>
                    </div>
                    <p className="text-gray-700 mt-1">{a.action}</p>
                  </div>
                  <div className="text-right whitespace-nowrap">
                    {a.estimated_savings_eur > 0 && (
                      <div className="text-green-600 font-medium">
                        {a.estimated_savings_eur.toLocaleString('tr-TR', { maximumFractionDigits: 0 })} EUR/yıl
                      </div>
                    )}
                    {a.estimated_investment_eur > 0 && (
                      <div className="text-xs text-gray-500">
                        Yatırım: {a.estimated_investment_eur.toLocaleString('tr-TR', { maximumFractionDigits: 0 })} EUR
                      </div>
                    )}
                    {a.payback_years < 99 && (
                      <div className="text-xs text-gray-500">GOS: {a.payback_years.toFixed(1)} yıl</div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
};

/* ---------- Main Component ---------- */
const EnergyManagementTab = ({ emData, onRerun, isLoading }) => {
  if (!emData || !emData.is_valid) return null;

  return (
    <Card
      title={
        <div className="flex items-center gap-2">
          <Shield className="w-5 h-5 text-blue-600" />
          <span>Enerji Yonetimi (ISO 50001)</span>
          {onRerun && (
            <button
              onClick={onRerun}
              disabled={isLoading}
              className="ml-auto text-xs px-2 py-1 border rounded hover:bg-gray-50 text-gray-600 flex items-center gap-1"
            >
              <RefreshCw className={`w-3 h-3 ${isLoading ? 'animate-spin' : ''}`} />
              Yeniden
            </button>
          )}
        </div>
      }
    >
      {/* Maturity Score */}
      <MaturityBar
        score={emData.maturity_score}
        level={emData.maturity_level}
        label={emData.maturity_level_label}
      />

      {/* EnPI Cards */}
      <EnPICards enpi={emData.enpi} />

      {/* Radar Charts */}
      <DualRadarCharts
        maturityRadar={emData.maturity_radar_data}
        enpiRadar={emData.enpi_radar_data}
      />

      {/* Gap Analysis */}
      <GapAnalysis dimensions={emData.maturity_dimensions} />

      {/* Warnings */}
      {emData.warnings && emData.warnings.length > 0 && (
        <div className="mb-4 space-y-2">
          {emData.warnings.map((w, i) => (
            <div key={i} className="flex items-start gap-2 bg-red-50 border border-red-200 rounded-lg p-3 text-sm text-red-700">
              <AlertTriangle className="w-4 h-4 mt-0.5 flex-shrink-0" />
              {w}
            </div>
          ))}
        </div>
      )}

      {/* Action Plan */}
      <ActionPlan
        actions={emData.action_plan}
        summary={emData.action_summary}
      />
    </Card>
  );
};

export default EnergyManagementTab;
