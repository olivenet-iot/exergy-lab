import FormField from './FormField';
import LoadingSpinner from '../common/Loading';

const ParameterForm = ({ fields, values, onChange, onSubmit, loading }) => {
  return (
    <form onSubmit={onSubmit} className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {fields?.map((field) => (
          <FormField
            key={field.id}
            field={field}
            value={values[field.id]}
            onChange={(value) => onChange(field.id, value)}
          />
        ))}
      </div>

      <button
        type="submit"
        disabled={loading}
        className={`
          w-full py-3 px-6 rounded-lg font-semibold text-white
          transition-all duration-200
          ${loading
            ? 'bg-gray-400 cursor-not-allowed'
            : 'bg-primary-600 hover:bg-primary-700 active:scale-[0.98]'
          }
        `}
      >
        {loading ? (
          <span className="flex items-center justify-center gap-2">
            <LoadingSpinner size="small" />
            Hesaplanıyor...
          </span>
        ) : (
          'Exergy Analizi Yap'
        )}
      </button>
    </form>
  );
};

export default ParameterForm;
