export const getPerformanceColor = (efficiency) => {
  if (efficiency >= 80) return 'emerald';
  if (efficiency >= 60) return 'blue';
  if (efficiency >= 40) return 'amber';
  return 'red';
};

export const getPerformanceHex = (efficiency) => {
  if (efficiency >= 80) return '#059669';
  if (efficiency >= 60) return '#2563eb';
  if (efficiency >= 40) return '#f59e0b';
  return '#ef4444';
};

export const getGradeInfo = (gradeLetter) => {
  const grades = {
    A: { label: 'Mukemmel', colorClass: 'text-green-700 bg-green-100' },
    B: { label: 'Iyi', colorClass: 'text-blue-700 bg-blue-100' },
    C: { label: 'Orta', colorClass: 'text-amber-700 bg-amber-100' },
    D: { label: 'Zayif', colorClass: 'text-orange-700 bg-orange-100' },
    F: { label: 'Kritik', colorClass: 'text-red-700 bg-red-100' },
  };
  return grades[gradeLetter] || { label: '', colorClass: 'text-gray-700 bg-gray-100' };
};
