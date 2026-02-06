import { formatNumber } from '../../utils/formatters';

const StreamTable = ({ streams }) => {
  if (!streams || streams.length === 0) {
    return (
      <div className="text-center py-4 text-gray-400 text-sm">
        Termal akış bulunamadı
      </div>
    );
  }

  const sorted = [...streams].sort((a, b) => b.Q_dot_kW - a.Q_dot_kW);

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b border-gray-200 text-left text-gray-500">
            <th className="py-2 px-2">#</th>
            <th className="py-2 px-2">Ekipman</th>
            <th className="py-2 px-2">Tip</th>
            <th className="py-2 px-2 text-right">T_giriş (°C)</th>
            <th className="py-2 px-2 text-right">T_çıkış (°C)</th>
            <th className="py-2 px-2 text-right">Q (kW)</th>
            <th className="py-2 px-2 text-right">CP (kW/K)</th>
          </tr>
        </thead>
        <tbody>
          {sorted.map((s, i) => (
            <tr
              key={s.stream_id}
              className={`border-b border-gray-100 ${
                s.stream_type === 'hot' ? 'bg-red-50' : 'bg-blue-50'
              }`}
            >
              <td className="py-1.5 px-2 text-gray-400">{i + 1}</td>
              <td className="py-1.5 px-2 font-medium text-gray-700">
                {s.equipment_name}
              </td>
              <td className="py-1.5 px-2">
                <span
                  className={`inline-block px-1.5 py-0.5 rounded text-xs font-medium ${
                    s.stream_type === 'hot'
                      ? 'bg-red-100 text-red-700'
                      : 'bg-blue-100 text-blue-700'
                  }`}
                >
                  {s.stream_type === 'hot' ? 'Sıcak' : 'Soğuk'}
                </span>
              </td>
              <td className="py-1.5 px-2 text-right font-mono">
                {formatNumber(s.T_supply_C, 1)}
              </td>
              <td className="py-1.5 px-2 text-right font-mono">
                {formatNumber(s.T_target_C, 1)}
              </td>
              <td className="py-1.5 px-2 text-right font-mono font-semibold">
                {formatNumber(s.Q_dot_kW, 1)}
              </td>
              <td className="py-1.5 px-2 text-right font-mono text-gray-500">
                {formatNumber(s.CP_kW_per_K, 3)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StreamTable;
