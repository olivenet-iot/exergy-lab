const SubtypeSelector = ({ subtypes, selected, onSelect }) => {
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      {subtypes?.map((subtype) => {
        const id = subtype.id || subtype.type;
        const name = subtype.name || subtype.label || id;
        const isSelected = selected === id;

        return (
          <button
            key={id}
            onClick={() => onSelect(id)}
            className={`
              p-4 rounded-xl border-2 transition-all duration-200
              flex flex-col items-center gap-2
              ${isSelected
                ? 'border-primary-500 bg-primary-50 text-primary-700'
                : 'border-gray-200 bg-white hover:border-gray-300'
              }
            `}
          >
            <span className="font-medium text-sm">{name}</span>
          </button>
        );
      })}
    </div>
  );
};

export default SubtypeSelector;
