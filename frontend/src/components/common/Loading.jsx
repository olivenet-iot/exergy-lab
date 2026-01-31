const sizeClasses = {
  small: 'w-4 h-4 border-2',
  medium: 'w-8 h-8 border-2',
  large: 'w-12 h-12 border-3',
};

const LoadingSpinner = ({ size = 'medium' }) => {
  return (
    <div
      className={`${sizeClasses[size]} border-gray-200 border-t-primary-600 rounded-full animate-spin`}
    />
  );
};

export default LoadingSpinner;
