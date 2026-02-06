import Card from '../common/Card';
import SankeyDiagram from '../results/SankeyDiagram';
import BenchmarkChart from '../results/BenchmarkChart';
import DetailedMetrics from '../results/DetailedMetrics';

const FlowTab = ({ result }) => {
  if (!result) return null;

  const { metrics = {}, heat_recovery = {}, benchmark = {}, sankey } = result;

  return (
    <div className="space-y-6">
      {/* Sankey Diagram (full width) */}
      <Card title="Ekserji Akış Diyagramı">
        <SankeyDiagram data={sankey} />
      </Card>

      {/* Benchmark (full width) */}
      <Card title="Benchmark Karşılaştırma">
        <BenchmarkChart
          efficiency={metrics.exergy_efficiency_percent}
          rating={benchmark.rating}
          percentile={benchmark.percentile}
        />
        {benchmark.comparison_text && (
          <p className="mt-4 text-sm text-gray-600">{benchmark.comparison_text}</p>
        )}
      </Card>

      {/* Detailed Metrics (full width) */}
      <DetailedMetrics metrics={metrics} heatRecovery={heat_recovery} />
    </div>
  );
};

export default FlowTab;
