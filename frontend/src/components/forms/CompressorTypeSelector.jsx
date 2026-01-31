import { Settings, CircleDot, Waves, RotateCw } from 'lucide-react';

const COMPRESSOR_ICONS = {
  screw: Settings,
  piston: CircleDot,
  scroll: Waves,
  centrifugal: RotateCw,
};

const CompressorTypeSelector = ({ types, selected, onSelect }) => {
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      {types.map((type) => {
        const Icon = COMPRESSOR_ICONS[type.id] || Settings;
        const isSelected = selected === type.id;

        return (
          <button
            key={type.id}
            onClick={() => onSelect(type.id)}
            className={`
              p-4 rounded-xl border-2 transition-all duration-200
              flex flex-col items-center gap-2
              ${isSelected
                ? 'border-primary-500 bg-primary-50 text-primary-700'
                : 'border-gray-200 bg-white hover:border-gray-300'
              }
            `}
          >
            <Icon className={`w-8 h-8 ${isSelected ? 'text-primary-600' : 'text-gray-400'}`} />
            <span className="font-medium text-sm">{type.name}</span>
          </button>
        );
      })}
    </div>
  );
};

export default CompressorTypeSelector;
