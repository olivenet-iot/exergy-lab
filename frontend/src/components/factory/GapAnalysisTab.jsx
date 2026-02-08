import { useState } from 'react';
import { Target, AlertTriangle, TrendingDown, Award, DollarSign, FileText, Edit3, Info, Plus } from 'lucide-react';
import Plot from 'react-plotly.js';
import Card from '../common/Card';
import { formatNumber, formatCurrency } from '../../utils/formatters';

/* ---------- ESI Grade styles ---------- */
const GRADE_COLORS = {
  A: { bg: 'bg-emerald-100', text: 'text-emerald-700', border: 'border-emerald-300', ring: 'ring-emerald-500' },
  B: { bg: 'bg-green-100', text: 'text-green-700', border: 'border-green-300', ring: 'ring-green-500' },
  C: { bg: 'bg-lime-100', text: 'text-lime-700', border: 'border-lime-300', ring: 'ring-lime-500' },
  D: { bg: 'bg-amber-100', text: 'text-amber-700', border: 'border-amber-300', ring: 'ring-amber-500' },
  E: { bg: 'bg-orange-100', text: 'text-orange-700', border: 'border-orange-300', ring: 'ring-orange-500' },
  F: { bg: 'bg-red-100', text: 'text-red-700', border: 'border-red-300', ring: 'ring-red-500' },
};

const PROCESS_TYPE_LABELS = {
  drying: 'Kurutma',
  heating: 'Isıtma',
  cooling: 'Soğutma',
  steam_generation: 'Buhar Üretimi',
  compressed_air: 'Basınçlı Hava',
  chp: 'Kojenerasyon (CHP)',
  cold_storage: 'Soğuk Depo',
  general_manufacturing: 'Genel Üretim',
};

const PRIORITY_STYLES = {
  critical: 'bg-red-100 text-red-700',
  high: 'bg-orange-100 text-orange-700',
  medium: 'bg-amber-100 text-amber-700',
  low: 'bg-green-100 text-green-700',
};

/* ---------- Plotly shared config ---------- */
const PLOTLY_CONFIG = { responsive: true, displayModeBar: false };
const PLOTLY_LAYOUT_BASE = {
  paper_bgcolor: 'transparent',
  plot_bgcolor: 'transparent',
  font: { family: 'Inter, system-ui, sans-serif', size: 12 },
};

/* ---------- Sub-components ---------- */

const ProcessCard = ({ gap, project, onEdit }) => (
  <Card>
    <div className="flex items-start justify-between mb-3">
      <div className="flex items-center gap-2">
        <Target className="w-5 h-5 text-cyan-600" />
        <h3 className="font-semibold text-gray-900">Proses Tanımı</h3>
      </div>
      {onEdit && (
        <button
          onClick={onEdit}
          className="flex items-center gap-1 text-sm text-cyan-600 hover:text-cyan-700"
        >
          <Edit3 className="w-3.5 h-3.5" />
          Düzenle
        </button>
      )}
    </div>
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      <div>
        <span className="text-xs text-gray-500 uppercase tracking-wider">Proses Tipi</span>
        <p className="font-medium text-gray-900">{PROCESS_TYPE_LABELS[gap.process_type] || gap.process_type}</p>
      </div>
      <div>
        <span className="text-xs text-gray-500 uppercase tracking-wider">Etiket</span>
        <p className="font-medium text-gray-900">{gap.process_label || '—'}</p>
      </div>
      <div>
        <span className="text-xs text-gray-500 uppercase tracking-wider">Alt Kategori</span>
        <p className="font-medium text-gray-900">{gap.subcategory || 'general'}</p>
      </div>
      <div>
        <span className="text-xs text-gray-500 uppercase tracking-wider">Çalışma Saati</span>
        <p className="font-medium text-gray-900">{formatNumber(gap.operating_hours, 0)} saat/yıl</p>
      </div>
    </div>
  </Card>
);

const ESIScoreCard = ({ gap }) => {
  const grade = gap.grade || 'F';
  const colors = GRADE_COLORS[grade] || GRADE_COLORS.F;
  const esi = gap.exergetic_sustainability_index;

  return (
    <Card>
      <div className="flex items-center gap-2 mb-4">
        <Award className="w-5 h-5 text-cyan-600" />
        <h3 className="font-semibold text-gray-900">Exergetik Sürdürülebilirlik Endeksi (ESI)</h3>
      </div>
      <div className="flex items-center gap-6">
        <div className={`flex items-center justify-center w-20 h-20 rounded-2xl ${colors.bg} ${colors.border} border-2`}>
          <span className={`text-4xl font-bold ${colors.text}`}>{grade}</span>
        </div>
        <div>
          <p className="text-3xl font-bold font-mono text-gray-900">{formatNumber(esi, 3)}</p>
          <p className="text-sm text-gray-500 mt-1">{gap.grade_description}</p>
        </div>
      </div>
    </Card>
  );
};

const ComparisonBarChart = ({ data }) => {
  if (!data?.categories || !data?.values) return null;

  const traces = [{
    x: data.values,
    y: data.categories,
    type: 'bar',
    orientation: 'h',
    marker: { color: data.colors },
    text: data.values.map(v => `${formatNumber(v, 1)} kW`),
    textposition: 'auto',
    hoverinfo: 'y+text',
  }];

  const layout = {
    ...PLOTLY_LAYOUT_BASE,
    xaxis: {
      title: 'Exergy (kW)',
      type: 'log',
      zeroline: false,
    },
    yaxis: { automargin: true },
    margin: { l: 120, r: 30, t: 10, b: 50 },
    height: 200,
  };

  return (
    <Plot
      data={traces}
      layout={layout}
      config={PLOTLY_CONFIG}
      style={{ width: '100%', height: '200px' }}
    />
  );
};

const WaterfallChart = ({ data }) => {
  if (!data?.labels || !data?.values) return null;

  const traces = [{
    type: 'waterfall',
    x: data.labels,
    y: data.values,
    measure: data.types,
    connector: { line: { color: '#e2e8f0', width: 1 } },
    increasing: { marker: { color: '#f59e0b' } },
    decreasing: { marker: { color: '#10b981' } },
    totals: { marker: { color: '#ef4444' } },
    text: data.values.map(v => `${formatNumber(Math.abs(v), 1)}`),
    textposition: 'outside',
    textfont: { size: 10 },
  }];

  const layout = {
    ...PLOTLY_LAYOUT_BASE,
    xaxis: { automargin: true },
    yaxis: { title: 'Exergy (kW)' },
    margin: { l: 60, r: 20, t: 10, b: 80 },
    height: 320,
    showlegend: false,
  };

  return (
    <Plot
      data={traces}
      layout={layout}
      config={PLOTLY_CONFIG}
      style={{ width: '100%', height: '320px' }}
    />
  );
};

const GapDonutChart = ({ data }) => {
  if (!data?.labels || !data?.values) return null;

  const traces = [{
    labels: data.labels,
    values: data.values,
    type: 'pie',
    hole: 0.5,
    marker: {
      colors: ['#ef4444', '#f97316', '#f59e0b', '#eab308', '#84cc16', '#22c55e', '#14b8a6', '#94a3b8'],
    },
    textinfo: 'label+percent',
    textposition: 'outside',
    textfont: { size: 10 },
    hovertemplate: '%{label}<br>%{value:.1f} kW (%{percent})<extra></extra>',
  }];

  const layout = {
    ...PLOTLY_LAYOUT_BASE,
    margin: { l: 20, r: 20, t: 10, b: 10 },
    height: 300,
    showlegend: false,
  };

  return (
    <Plot
      data={traces}
      layout={layout}
      config={PLOTLY_CONFIG}
      style={{ width: '100%', height: '300px' }}
    />
  );
};

const GapDistributionTable = ({ distribution }) => {
  if (!distribution || distribution.length === 0) return null;

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b border-gray-200 text-gray-500 text-xs uppercase tracking-wider">
            <th className="py-2 text-left">Ekipman</th>
            <th className="py-2 text-right">Yıkım (kW)</th>
            <th className="py-2 text-right">Pay (%)</th>
            <th className="py-2 text-right">Kümülatif (%)</th>
            <th className="py-2 text-center">Öncelik</th>
          </tr>
        </thead>
        <tbody>
          {distribution.map((item, i) => (
            <tr key={i} className="border-b border-gray-100">
              <td className="py-2 font-medium text-gray-900">{item.equipment_name}</td>
              <td className="py-2 text-right font-mono text-red-600">{formatNumber(item.destroyed_kW, 1)}</td>
              <td className="py-2 text-right font-mono">{formatNumber(item.gap_share_pct, 1)}%</td>
              <td className="py-2 text-right font-mono">{formatNumber(item.cumulative_pct, 1)}%</td>
              <td className="py-2 text-center">
                <span className={`inline-block px-2 py-0.5 rounded text-xs font-medium ${PRIORITY_STYLES[item.priority] || ''}`}>
                  {item.priority}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

/* ---------- Empty state when no process ---------- */
const NoProcessState = ({ onAddProcess }) => (
  <div className="bg-amber-50 border border-amber-200 rounded-xl p-8">
    <div className="flex flex-col items-center text-center">
      <div className="w-14 h-14 rounded-full bg-amber-100 flex items-center justify-center mb-4">
        <Target className="w-7 h-7 text-amber-600" />
      </div>
      <h3 className="text-lg font-semibold text-amber-800 mb-2">Proses tanımı eklenmemiş</h3>
      <p className="text-sm text-amber-700 mb-4 max-w-md">
        Proses tanımı ekleyerek tesisinizin termodinamik ideale ve en iyi teknolojiye (BAT) ne kadar uzak olduğunu öğrenebilirsiniz.
      </p>
      <ul className="text-sm text-amber-700 mb-5 space-y-1">
        <li>Termodinamik minimum ile kıyaslama</li>
        <li>BAT (En İyi Mevcut Teknoloji) referansı</li>
        <li>ESI sürdürülebilirlik notu (A-F)</li>
        <li>Yıllık tasarruf potansiyeli hesabı</li>
      </ul>
      {onAddProcess && (
        <button
          onClick={onAddProcess}
          className="flex items-center gap-2 px-5 py-2.5 bg-amber-600 text-white rounded-lg hover:bg-amber-700 transition-colors"
        >
          <Plus className="w-4 h-4" />
          Proses Tanımı Ekle
        </button>
      )}
    </div>
  </div>
);

/* ---------- Main component ---------- */
const GapAnalysisTab = ({ analysisResult, project, onAddProcess, onEditProcess }) => {
  const gap = analysisResult?.gap_analysis;

  // No process defined
  if (!project?.process_type) {
    return <NoProcessState onAddProcess={onAddProcess} />;
  }

  // Process defined but no gap data yet (analysis not run or failed)
  if (!gap) {
    return (
      <div className="flex flex-col items-center justify-center py-16 text-center">
        <div className="w-12 h-12 rounded-full bg-slate-100 flex items-center justify-center mb-4">
          <Info className="w-5 h-5 text-slate-400" />
        </div>
        <p className="text-slate-500 mb-2">Proses tanımı mevcut ancak gap analizi henüz çalıştırılmadı.</p>
        <p className="text-sm text-slate-400">Fabrika analizini tekrar çalıştırarak gap verisi oluşturabilirsiniz.</p>
      </div>
    );
  }

  const [showDetails, setShowDetails] = useState(false);

  return (
    <div className="space-y-6">
      {/* Process Card */}
      <ProcessCard gap={gap} project={project} onEdit={onEditProcess} />

      {/* ESI Score + 3-Layer Comparison side by side */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <ESIScoreCard gap={gap} />

        <Card>
          <div className="flex items-center gap-2 mb-4">
            <TrendingDown className="w-5 h-5 text-cyan-600" />
            <h3 className="font-semibold text-gray-900">3 Katmanlı Karşılaştırma</h3>
          </div>
          <ComparisonBarChart data={gap.comparison_bar_data} />
          <div className="grid grid-cols-3 gap-4 mt-4 text-center text-sm">
            <div>
              <p className="text-xs text-gray-500 uppercase">Minimum</p>
              <p className="font-mono font-semibold text-emerald-600">{formatNumber(gap.minimum_exergy_kW, 1)} kW</p>
            </div>
            <div>
              <p className="text-xs text-gray-500 uppercase">BAT</p>
              <p className="font-mono font-semibold text-amber-600">{formatNumber(gap.bat_exergy_kW, 1)} kW</p>
            </div>
            <div>
              <p className="text-xs text-gray-500 uppercase">Mevcut</p>
              <p className="font-mono font-semibold text-red-600">{formatNumber(gap.actual_exergy_kW, 1)} kW</p>
            </div>
          </div>
        </Card>
      </div>

      {/* Waterfall + Donut side by side */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <Card>
            <div className="flex items-center gap-2 mb-4">
              <AlertTriangle className="w-5 h-5 text-cyan-600" />
              <h3 className="font-semibold text-gray-900">Gap Waterfall</h3>
            </div>
            <WaterfallChart data={gap.waterfall_data} />
          </Card>
        </div>
        <Card>
          <div className="flex items-center gap-2 mb-4">
            <Target className="w-5 h-5 text-cyan-600" />
            <h3 className="font-semibold text-gray-900">Gap Dağılımı</h3>
          </div>
          <GapDonutChart data={gap.gap_pie_data} />
        </Card>
      </div>

      {/* Economic Impact */}
      <Card>
        <div className="flex items-center gap-2 mb-4">
          <DollarSign className="w-5 h-5 text-cyan-600" />
          <h3 className="font-semibold text-gray-900">Ekonomik Etki</h3>
        </div>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
          <div>
            <span className="text-xs text-gray-500 uppercase tracking-wider">Toplam Gap Maliyeti</span>
            <p className="text-xl font-bold font-mono text-red-600">{formatCurrency(gap.annual_total_gap_cost_eur)}/yıl</p>
          </div>
          <div>
            <span className="text-xs text-gray-500 uppercase tracking-wider">BAT Gap Maliyeti</span>
            <p className="text-xl font-bold font-mono text-amber-600">{formatCurrency(gap.annual_bat_gap_cost_eur)}/yıl</p>
          </div>
          <div>
            <span className="text-xs text-gray-500 uppercase tracking-wider">BAT Teknolojisi</span>
            <p className="font-medium text-gray-900">{gap.bat_technology || '—'}</p>
            {gap.bat_source && <p className="text-xs text-gray-500 mt-1">{gap.bat_source}</p>}
          </div>
          <div>
            <span className="text-xs text-gray-500 uppercase tracking-wider">BAT Verimi</span>
            <p className="text-xl font-bold font-mono text-emerald-600">%{formatNumber(gap.bat_efficiency_pct, 1)}</p>
          </div>
        </div>
      </Card>

      {/* Gap Distribution Table */}
      {gap.gap_distribution && gap.gap_distribution.length > 0 && (
        <Card>
          <div className="flex items-center gap-2 mb-4">
            <TrendingDown className="w-5 h-5 text-cyan-600" />
            <h3 className="font-semibold text-gray-900">Ekipman Bazlı Gap Dağılımı</h3>
          </div>
          <GapDistributionTable distribution={gap.gap_distribution} />
        </Card>
      )}

      {/* Calculation Details (collapsible) */}
      <Card>
        <button
          onClick={() => setShowDetails(!showDetails)}
          className="flex items-center gap-2 w-full text-left"
        >
          <FileText className="w-5 h-5 text-cyan-600" />
          <h3 className="font-semibold text-gray-900">Hesaplama Detayları</h3>
          <span className="ml-auto text-sm text-gray-500">{showDetails ? 'Gizle' : 'Göster'}</span>
        </button>
        {showDetails && (
          <div className="mt-4 space-y-3">
            <div>
              <span className="text-xs text-gray-500 uppercase tracking-wider">Yöntem</span>
              <p className="text-sm text-gray-700">{gap.min_exergy_method}</p>
            </div>
            {gap.min_exergy_assumptions && gap.min_exergy_assumptions.length > 0 && (
              <div>
                <span className="text-xs text-gray-500 uppercase tracking-wider">Varsayımlar</span>
                <ul className="list-disc list-inside text-sm text-gray-700 mt-1 space-y-0.5">
                  {gap.min_exergy_assumptions.map((a, i) => (
                    <li key={i}>{a}</li>
                  ))}
                </ul>
              </div>
            )}
            <div className="grid grid-cols-3 gap-4 pt-2 border-t border-gray-100">
              <div>
                <span className="text-xs text-gray-500">Spesifik Minimum</span>
                <p className="font-mono text-sm">{formatNumber(gap.specific_minimum, 2)} {gap.specific_unit}</p>
              </div>
              <div>
                <span className="text-xs text-gray-500">Spesifik BAT</span>
                <p className="font-mono text-sm">{formatNumber(gap.specific_bat, 2)} {gap.specific_unit}</p>
              </div>
              <div>
                <span className="text-xs text-gray-500">Spesifik Mevcut</span>
                <p className="font-mono text-sm">{formatNumber(gap.specific_actual, 2)} {gap.specific_unit}</p>
              </div>
            </div>
          </div>
        )}
      </Card>
    </div>
  );
};

export default GapAnalysisTab;
