export const formatNumber = (value, decimals = 1) => {
  if (value == null || isNaN(value)) return '—';
  return Number(value).toLocaleString('tr-TR', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
};

export const formatCurrency = (value, currency = 'EUR') => {
  if (value == null || isNaN(value)) return '—';
  return Number(value).toLocaleString('tr-TR', {
    style: 'currency',
    currency,
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  });
};

export const formatPercentage = (value, decimals = 1) => {
  if (value == null || isNaN(value)) return '—';
  return `${Number(value).toFixed(decimals)}%`;
};
