import { Trash2, Wind, Flame, Snowflake, Droplets, ArrowLeftRight, Zap, Sun } from 'lucide-react';

const EQUIPMENT_ICONS = {
  compressor: Wind,
  boiler: Flame,
  chiller: Snowflake,
  pump: Droplets,
  heat_exchanger: ArrowLeftRight,
  steam_turbine: Zap,
  dryer: Sun,
};

const EQUIPMENT_LABELS = {
  compressor: 'Kompresor',
  boiler: 'Kazan',
  chiller: 'Chiller',
  pump: 'Pompa',
  heat_exchanger: 'Isı Eşanjörü',
  steam_turbine: 'Buhar Türbini',
  dryer: 'Kurutma Fırını',
};

const EquipmentInventory = ({ equipment, onRemove }) => {
  if (!equipment || equipment.length === 0) {
    return (
      <div className="text-center py-6 text-gray-500">
        Henuz ekipman eklenmedi.
      </div>
    );
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b border-gray-200">
            <th className="text-left py-2 px-3 text-gray-600 font-medium">Ad</th>
            <th className="text-left py-2 px-3 text-gray-600 font-medium">Tip</th>
            <th className="text-left py-2 px-3 text-gray-600 font-medium">Alt Tip</th>
            <th className="text-left py-2 px-3 text-gray-600 font-medium">Durum</th>
            <th className="text-right py-2 px-3"></th>
          </tr>
        </thead>
        <tbody>
          {equipment.map((eq) => {
            const Icon = EQUIPMENT_ICONS[eq.type] || Wind;
            const hasResult = !!eq.analysis_result;

            return (
              <tr key={eq.id} className="border-b border-gray-100 hover:bg-gray-50">
                <td className="py-2 px-3">
                  <div className="flex items-center gap-2">
                    <Icon className="w-4 h-4 text-gray-400" />
                    <span className="font-medium text-gray-900">{eq.name}</span>
                  </div>
                </td>
                <td className="py-2 px-3 text-gray-600">{EQUIPMENT_LABELS[eq.type] || eq.type}</td>
                <td className="py-2 px-3 text-gray-600">{eq.subtype}</td>
                <td className="py-2 px-3">
                  {hasResult ? (
                    <span className="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-green-100 text-green-700">
                      Analiz edildi
                    </span>
                  ) : (
                    <span className="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-gray-100 text-gray-500">
                      Bekliyor
                    </span>
                  )}
                </td>
                <td className="py-2 px-3 text-right">
                  {onRemove && (
                    <button
                      onClick={() => onRemove(eq.id)}
                      className="p-1 text-red-500 hover:bg-red-50 rounded transition-colors"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default EquipmentInventory;
