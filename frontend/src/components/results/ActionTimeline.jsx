import { Zap, Calendar, Target } from 'lucide-react';

const TimelineColumn = ({ icon: Icon, title, items, iconColor, borderColor }) => {
  if (!items || items.length === 0) return null;

  return (
    <div className={`border-t-2 ${borderColor} pt-3`}>
      <div className="flex items-center gap-2 mb-3">
        <Icon className={`w-4 h-4 ${iconColor}`} />
        <span className="text-sm font-semibold text-gray-700">{title}</span>
      </div>
      <ul className="space-y-2">
        {items.map((item, i) => (
          <li key={i} className="text-sm text-gray-600 flex items-start gap-2">
            <span className={`w-1.5 h-1.5 rounded-full mt-1.5 flex-shrink-0 ${iconColor.replace('text-', 'bg-')}`} />
            {item}
          </li>
        ))}
      </ul>
    </div>
  );
};

const ActionTimeline = ({ actionPlan }) => {
  if (!actionPlan) return null;

  const { immediate = [], short_term = [], medium_term = [] } = actionPlan;
  if (immediate.length === 0 && short_term.length === 0 && medium_term.length === 0) {
    return null;
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <TimelineColumn
        icon={Zap}
        title="Hemen"
        items={immediate}
        iconColor="text-red-500"
        borderColor="border-red-400"
      />
      <TimelineColumn
        icon={Calendar}
        title="1-3 Ay"
        items={short_term}
        iconColor="text-amber-500"
        borderColor="border-amber-400"
      />
      <TimelineColumn
        icon={Target}
        title="3-12 Ay"
        items={medium_term}
        iconColor="text-blue-500"
        borderColor="border-blue-400"
      />
    </div>
  );
};

export default ActionTimeline;
