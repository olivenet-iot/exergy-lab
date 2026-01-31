import { formatNumber } from '../../utils/formatters';
import Card from '../common/Card';
import MetricsCard from './MetricsCard';
import SankeyDiagram from './SankeyDiagram';
import BenchmarkChart from './BenchmarkChart';

const ResultsPanel = ({ data }) => {
  if (!data) return null;

  const { metrics = {}, heat_recovery = {}, benchmark = {}, sankey } = data;

  return (
    <div className="space-y-6">
      {/* Metric Cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <MetricsCard
          title="Exergy Verimi"
          value={metrics?.exergy_efficiency_percent}
          unit="%"
          rating={benchmark?.rating}
          icon="gauge"
        />
        <MetricsCard
          title="Exergy Girisi"
          value={metrics?.exergy_input_kW}
          unit="kW"
          icon="zap"
        />
        <MetricsCard
          title="Faydali Exergy"
          value={metrics?.exergy_output_kW}
          unit="kW"
          icon="check-circle"
        />
        <MetricsCard
          title="Exergy Yikimi"
          value={metrics?.exergy_destroyed_kW}
          unit="kW"
          icon="x-circle"
        />
      </div>

      {/* Sankey Diagram */}
      <Card title="Exergy Akis Diyagrami">
        <SankeyDiagram data={sankey} />
      </Card>

      {/* Annual Impact & Benchmark */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="Yillik Etki">
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Yillik Kayip</span>
              <span className="font-mono font-semibold text-red-600">
                {formatNumber(metrics?.annual_loss_kWh)} kWh
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Yillik Maliyet</span>
              <span className="font-mono font-semibold text-red-600">
                &euro;{formatNumber(metrics?.annual_cost_eur)}
              </span>
            </div>
            <hr />
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Isi Geri Kazanim Potansiyeli</span>
              <span className="font-mono font-semibold text-amber-600">
                {formatNumber(heat_recovery?.potential_kW)} kW
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Potansiyel Tasarruf</span>
              <span className="font-mono font-semibold text-green-600">
                &euro;{formatNumber(heat_recovery?.annual_savings_eur)}/yil
              </span>
            </div>
          </div>
        </Card>

        <Card title="Benchmark Karsilastirma">
          <BenchmarkChart
            efficiency={metrics?.exergy_efficiency_percent}
            rating={benchmark?.rating}
            percentile={benchmark?.percentile}
          />
          <p className="mt-4 text-sm text-gray-600">
            {benchmark?.comparison_text}
          </p>
        </Card>
      </div>
    </div>
  );
};

export default ResultsPanel;
