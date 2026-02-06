import Card from '../common/Card';
import SankeyDiagram from '../results/SankeyDiagram';
import BenchmarkChart from '../results/BenchmarkChart';
import DetailedMetrics from '../results/DetailedMetrics';

const FlowTab = ({ result }) => {
  if (!result) return null;

  const { metrics = {}, heat_recovery = {}, benchmark = {}, sankey } = result;

  return (
    <div className="space-y-6">
      {/* Sankey Diagram (full width, top) */}
      <Card title="Exergy Akis Diyagrami">
        <SankeyDiagram data={sankey} />
      </Card>

      {/* Two-column: Benchmark (left) + DetailedMetrics (right) */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div>
          <Card title="Benchmark Karsilastirma">
            <BenchmarkChart
              efficiency={metrics.exergy_efficiency_percent}
              rating={benchmark.rating}
              percentile={benchmark.percentile}
            />
            {benchmark.comparison_text && (
              <p className="mt-4 text-sm text-gray-600">{benchmark.comparison_text}</p>
            )}
          </Card>
        </div>

        <div>
          <DetailedMetrics metrics={metrics} heatRecovery={heat_recovery} />
        </div>
      </div>
    </div>
  );
};

export default FlowTab;
