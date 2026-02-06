import SankeyDiagram from '../results/SankeyDiagram';
import { formatNumber, formatPercentage } from '../../utils/formatters';

const FactorySankey = ({ data }) => {
  if (!data || !data.nodes || !data.links) {
    return (
      <div className="h-64 flex items-center justify-center text-gray-400">
        Sankey verisi bulunamadı
      </div>
    );
  }

  return (
    <div>
      {/* Larger height for factory-level view */}
      <div className="h-[420px]">
        <SankeyDiagram data={data} />
      </div>

      {/* Summary stats */}
      {data.summary && (
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4 pt-4 border-t border-gray-100">
          <div className="text-center">
            <div className="text-xs text-gray-500">Toplam Giriş</div>
            <div className="text-sm font-mono font-semibold text-gray-900">
              {formatNumber(data.summary.total_input_kW, 1)} kW
            </div>
          </div>
          <div className="text-center">
            <div className="text-xs text-gray-500">Faydalı Çıkış</div>
            <div className="text-sm font-mono font-semibold text-green-600">
              {formatNumber(data.summary.useful_output_kW, 1)} kW
            </div>
          </div>
          <div className="text-center">
            <div className="text-xs text-gray-500">Toplam Kayıp</div>
            <div className="text-sm font-mono font-semibold text-red-600">
              {formatNumber(data.summary.irreversibility_kW, 1)} kW
            </div>
          </div>
          <div className="text-center">
            <div className="text-xs text-gray-500">Fabrika Verimi</div>
            <div className="text-sm font-mono font-semibold text-cyan-600">
              {formatPercentage(data.summary.efficiency_pct)}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default FactorySankey;
