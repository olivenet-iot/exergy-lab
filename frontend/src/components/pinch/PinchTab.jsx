import { useState } from 'react';
import { Thermometer, RefreshCw } from 'lucide-react';
import Card from '../common/Card';
import PinchMetricBar from './PinchMetricBar';
import CompositeCurveChart from './CompositeCurveChart';
import GrandCompositeCurveChart from './GrandCompositeCurveChart';
import StreamTable from './StreamTable';
import HENMatches from './HENMatches';

const PinchTab = ({ pinchData, onRerun, isLoading }) => {
  const [deltaTMin, setDeltaTMin] = useState(pinchData?.delta_T_min_C || 10);

  if (!pinchData?.is_valid) {
    const msg = pinchData?.error_message || 'Pinch analizi icin yeterli termal akis yok';
    return (
      <Card title="Pinch Analizi">
        <div className="text-center py-8">
          <Thermometer className="w-10 h-10 text-gray-300 mx-auto mb-3" />
          <p className="text-gray-500 text-sm">{msg}</p>
          {pinchData?.streams?.length > 0 && (
            <p className="text-gray-400 text-xs mt-1">
              Mevcut akislar: {pinchData.hot_stream_count} sicak, {pinchData.cold_stream_count} soguk
            </p>
          )}
        </div>
      </Card>
    );
  }

  const handleRerun = () => {
    if (onRerun) onRerun({ delta_T_min_C: deltaTMin });
  };

  return (
    <div className="space-y-4">
      {/* Header with delta T control */}
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-semibold text-gray-800 flex items-center gap-2">
          <Thermometer className="w-5 h-5 text-purple-600" />
          Pinch Analizi
        </h3>
        {onRerun && (
          <div className="flex items-center gap-2">
            <label className="text-xs text-gray-500">
              ΔT<sub>min</sub>
            </label>
            <input
              type="number"
              min={1}
              max={50}
              step={1}
              value={deltaTMin}
              onChange={(e) => setDeltaTMin(Number(e.target.value))}
              className="w-16 px-2 py-1 text-sm border border-gray-300 rounded focus:ring-1 focus:ring-purple-500 focus:border-purple-500"
            />
            <span className="text-xs text-gray-400">°C</span>
            <button
              onClick={handleRerun}
              disabled={isLoading}
              className="flex items-center gap-1 px-3 py-1 text-sm bg-purple-600 text-white rounded hover:bg-purple-700 transition-colors disabled:opacity-50"
            >
              {isLoading ? (
                <div className="animate-spin rounded-full h-3 w-3 border-b-2 border-white" />
              ) : (
                <RefreshCw className="w-3 h-3" />
              )}
              Yeniden Calistir
            </button>
          </div>
        )}
      </div>

      {/* Metric Bar */}
      <PinchMetricBar pinch={pinchData} />

      {/* Charts: 2-column grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <Card title="Kompozit Egriler">
          <CompositeCurveChart data={pinchData.composite_curves} />
        </Card>
        <Card title="Grand Kompozit Egri (GCC)">
          <GrandCompositeCurveChart data={pinchData.grand_composite_curve} />
        </Card>
      </div>

      {/* Stream Table */}
      <Card title="Termal Akislar">
        <StreamTable streams={pinchData.streams} />
      </Card>

      {/* HEN Matches */}
      {pinchData.hen_matches?.length > 0 && (
        <Card title="HEN Eslestirme Onerileri">
          <HENMatches matches={pinchData.hen_matches} />
        </Card>
      )}
    </div>
  );
};

export default PinchTab;
