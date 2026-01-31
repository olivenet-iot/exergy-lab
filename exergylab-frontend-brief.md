# ExergyLab Frontend Brief

> **Claude Code için:** Bu dosyayı oku, ExergyLab projesi için React frontend geliştir.

---

## 🎯 Görev Özeti

ExergyLab projesi için modern React frontend oluştur. Backend API'yi (FastAPI, port 8000) kullanarak kompresör exergy analizi arayüzü yap.

**Hedef:**
- Temiz, modern, profesyonel görünüm
- Kompresör tipi seçimi ve dinamik form
- Exergy analiz sonuçları
- Sankey diyagramı (Plotly)
- Benchmark karşılaştırma
- Çözüm önerileri

---

## 📁 Proje Yapısı

```
exergy-lab/
├── frontend/                  # YENİ: React uygulaması
│   ├── src/
│   │   ├── components/
│   │   │   ├── layout/
│   │   │   │   ├── Header.jsx
│   │   │   │   ├── Footer.jsx
│   │   │   │   └── Layout.jsx
│   │   │   ├── forms/
│   │   │   │   ├── CompressorTypeSelector.jsx
│   │   │   │   ├── ParameterForm.jsx
│   │   │   │   └── FormField.jsx
│   │   │   ├── results/
│   │   │   │   ├── ResultsPanel.jsx
│   │   │   │   ├── MetricsCard.jsx
│   │   │   │   ├── SankeyDiagram.jsx
│   │   │   │   ├── BenchmarkChart.jsx
│   │   │   │   └── SolutionsList.jsx
│   │   │   └── common/
│   │   │       ├── Button.jsx
│   │   │       ├── Card.jsx
│   │   │       ├── Loading.jsx
│   │   │       └── Tooltip.jsx
│   │   ├── hooks/
│   │   │   ├── useAnalysis.js
│   │   │   └── useCompressorTypes.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── utils/
│   │   │   └── formatters.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
```

---

## 🛠️ BÖLÜM 1: Proje Kurulumu

### 1.1 Vite + React + Tailwind

```bash
cd exergy-lab
npm create vite@latest frontend -- --template react
cd frontend
npm install
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### 1.2 Dependencies

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-plotly.js": "^2.6.0",
    "plotly.js": "^2.29.0",
    "axios": "^1.6.0",
    "lucide-react": "^0.312.0"
  },
  "devDependencies": {
    "tailwindcss": "^3.4.0",
    "postcss": "^8.4.0",
    "autoprefixer": "^10.4.0",
    "@vitejs/plugin-react": "^4.2.0",
    "vite": "^5.0.0"
  }
}
```

### 1.3 Tailwind Config

```javascript
// tailwind.config.js
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
        },
        success: '#10b981',
        warning: '#f59e0b',
        danger: '#ef4444',
      }
    },
  },
  plugins: [],
}
```

---

## 🎨 BÖLÜM 2: Tasarım Sistemi

### 2.1 Renk Paleti

```
Primary (Mavi):     #2563eb - Ana aksiyonlar, linkler
Success (Yeşil):    #10b981 - Faydalı exergy, iyi sonuçlar
Warning (Sarı):     #f59e0b - Geri kazanılabilir ısı
Danger (Kırmızı):   #ef4444 - Exergy yıkımı, kötü sonuçlar
Neutral (Gri):      #6b7280 - Metin, borderlar

Background:         #f8fafc (açık gri)
Card Background:    #ffffff
Text Primary:       #1f2937
Text Secondary:     #6b7280
```

### 2.2 Sankey Renkleri

```javascript
const SANKEY_COLORS = {
  electricity: '#3b82f6',      // Mavi - Elektrik girişi
  compressor: '#6b7280',       // Gri - Kompresör (node)
  useful_exergy: '#10b981',    // Yeşil - Basınçlı hava (faydalı)
  recoverable_heat: '#f59e0b', // Sarı - Geri kazanılabilir ısı
  destroyed: '#ef4444',        // Kırmızı - Exergy yıkımı
}
```

### 2.3 Tipografi

```css
/* Başlıklar: Inter veya sistem fontu */
font-family: 'Inter', system-ui, sans-serif;

/* Sayılar/Metrikler: Monospace */
font-family: 'JetBrains Mono', monospace;
```

---

## 🧩 BÖLÜM 3: Components

### 3.1 Layout

#### Header.jsx
```jsx
const Header = () => {
  return (
    <header className="bg-white border-b border-gray-200 px-6 py-4">
      <div className="flex items-center justify-between max-w-7xl mx-auto">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-primary-600 rounded-lg flex items-center justify-center">
            <span className="text-white font-bold">Ex</span>
          </div>
          <div>
            <h1 className="text-xl font-bold text-gray-900">ExergyLab</h1>
            <p className="text-sm text-gray-500">Termodinamik Performans Analizi</p>
          </div>
        </div>
        {/* Sağ taraf: Ayarlar, dil seçimi vb. (opsiyonel) */}
      </div>
    </header>
  );
};
```

#### Layout.jsx
```jsx
const Layout = ({ children }) => {
  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main className="max-w-7xl mx-auto px-6 py-8">
        {children}
      </main>
      <Footer />
    </div>
  );
};
```

### 3.2 Kompresör Tipi Seçici

#### CompressorTypeSelector.jsx

```jsx
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
        const Icon = COMPRESSOR_ICONS[type.id];
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
```

### 3.3 Parametre Formu

#### ParameterForm.jsx

```jsx
const ParameterForm = ({ fields, values, onChange, onSubmit, loading }) => {
  return (
    <form onSubmit={onSubmit} className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {fields.map((field) => (
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
```

#### FormField.jsx

```jsx
const FormField = ({ field, value, onChange }) => {
  const { id, label, unit, type, required, min, max, step, help, default: defaultValue } = field;
  
  return (
    <div className="space-y-1">
      <label htmlFor={id} className="block text-sm font-medium text-gray-700">
        {label}
        {required && <span className="text-red-500 ml-1">*</span>}
        {unit && <span className="text-gray-400 ml-1">({unit})</span>}
      </label>
      
      <input
        id={id}
        type="number"
        value={value ?? defaultValue ?? ''}
        onChange={(e) => onChange(parseFloat(e.target.value) || null)}
        min={min}
        max={max}
        step={step || 'any'}
        required={required}
        className="
          w-full px-3 py-2 rounded-lg border border-gray-300
          focus:ring-2 focus:ring-primary-500 focus:border-primary-500
          transition-colors duration-200
        "
        placeholder={defaultValue ? `Varsayılan: ${defaultValue}` : ''}
      />
      
      {help && (
        <p className="text-xs text-gray-500">{help}</p>
      )}
    </div>
  );
};
```

### 3.4 Sonuç Paneli

#### ResultsPanel.jsx

```jsx
const ResultsPanel = ({ data }) => {
  if (!data) return null;
  
  const { metrics, heat_recovery, benchmark, sankey } = data;
  
  return (
    <div className="space-y-6">
      {/* Metrik Kartları */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <MetricsCard
          title="Exergy Verimi"
          value={metrics.exergy_efficiency_percent}
          unit="%"
          rating={benchmark.rating}
          icon="gauge"
        />
        <MetricsCard
          title="Exergy Girişi"
          value={metrics.exergy_input_kW}
          unit="kW"
          color="blue"
          icon="zap"
        />
        <MetricsCard
          title="Faydalı Exergy"
          value={metrics.exergy_output_kW}
          unit="kW"
          color="green"
          icon="check-circle"
        />
        <MetricsCard
          title="Exergy Yıkımı"
          value={metrics.exergy_destroyed_kW}
          unit="kW"
          color="red"
          icon="x-circle"
        />
      </div>
      
      {/* Sankey Diyagramı */}
      <Card title="Exergy Akış Diyagramı">
        <SankeyDiagram data={sankey} />
      </Card>
      
      {/* Yıllık Etki & Benchmark */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="Yıllık Etki">
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Yıllık Kayıp</span>
              <span className="font-mono font-semibold text-red-600">
                {formatNumber(metrics.annual_loss_kWh)} kWh
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Yıllık Maliyet</span>
              <span className="font-mono font-semibold text-red-600">
                €{formatNumber(metrics.annual_cost_eur)}
              </span>
            </div>
            <hr />
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Isı Geri Kazanım Potansiyeli</span>
              <span className="font-mono font-semibold text-amber-600">
                {formatNumber(heat_recovery.potential_kW)} kW
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Potansiyel Tasarruf</span>
              <span className="font-mono font-semibold text-green-600">
                €{formatNumber(heat_recovery.annual_savings_eur)}/yıl
              </span>
            </div>
          </div>
        </Card>
        
        <Card title="Benchmark Karşılaştırma">
          <BenchmarkChart 
            efficiency={metrics.exergy_efficiency_percent}
            rating={benchmark.rating}
            percentile={benchmark.percentile}
          />
          <p className="mt-4 text-sm text-gray-600">
            {benchmark.comparison_text}
          </p>
        </Card>
      </div>
    </div>
  );
};
```

### 3.5 Metrik Kartı

#### MetricsCard.jsx

```jsx
import { Gauge, Zap, CheckCircle, XCircle } from 'lucide-react';

const ICONS = {
  gauge: Gauge,
  zap: Zap,
  'check-circle': CheckCircle,
  'x-circle': XCircle,
};

const RATING_COLORS = {
  excellent: 'bg-green-100 text-green-800 border-green-200',
  good: 'bg-blue-100 text-blue-800 border-blue-200',
  average: 'bg-amber-100 text-amber-800 border-amber-200',
  poor: 'bg-red-100 text-red-800 border-red-200',
};

const MetricsCard = ({ title, value, unit, rating, color, icon }) => {
  const Icon = ICONS[icon];
  
  return (
    <div className="bg-white rounded-xl border border-gray-200 p-4">
      <div className="flex items-center justify-between mb-2">
        <span className="text-sm text-gray-500">{title}</span>
        {Icon && <Icon className="w-5 h-5 text-gray-400" />}
      </div>
      
      <div className="flex items-baseline gap-1">
        <span className="text-2xl font-bold font-mono">
          {typeof value === 'number' ? value.toFixed(1) : value}
        </span>
        <span className="text-gray-500">{unit}</span>
      </div>
      
      {rating && (
        <div className={`
          inline-block mt-2 px-2 py-0.5 rounded text-xs font-medium
          ${RATING_COLORS[rating]}
        `}>
          {rating === 'excellent' && 'Mükemmel'}
          {rating === 'good' && 'İyi'}
          {rating === 'average' && 'Ortalama'}
          {rating === 'poor' && 'Düşük'}
        </div>
      )}
    </div>
  );
};
```

### 3.6 Sankey Diyagramı

#### SankeyDiagram.jsx

```jsx
import Plot from 'react-plotly.js';

const SankeyDiagram = ({ data }) => {
  if (!data || !data.nodes || !data.links) {
    return <div className="h-64 flex items-center justify-center text-gray-400">Veri yükleniyor...</div>;
  }
  
  const plotData = [{
    type: 'sankey',
    orientation: 'h',
    node: {
      pad: 20,
      thickness: 30,
      line: { color: 'white', width: 2 },
      label: data.nodes.map(n => n.label),
      color: data.nodes.map(n => n.color),
    },
    link: {
      source: data.links.map(l => l.source),
      target: data.links.map(l => l.target),
      value: data.links.map(l => l.value),
      color: data.links.map(l => l.color),
    },
  }];
  
  const layout = {
    font: { family: 'Inter, system-ui, sans-serif', size: 12 },
    margin: { l: 20, r: 20, t: 20, b: 20 },
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
  };
  
  const config = {
    displayModeBar: false,
    responsive: true,
  };
  
  return (
    <div className="h-64 md:h-80">
      <Plot
        data={plotData}
        layout={layout}
        config={config}
        style={{ width: '100%', height: '100%' }}
      />
    </div>
  );
};
```

### 3.7 Benchmark Grafiği

#### BenchmarkChart.jsx

```jsx
const BenchmarkChart = ({ efficiency, rating, percentile }) => {
  // Benchmark aralıkları (vidalı kompresör için)
  const ranges = [
    { label: 'Düşük', max: 30, color: '#ef4444' },
    { label: 'Ortalama', max: 45, color: '#f59e0b' },
    { label: 'İyi', max: 55, color: '#3b82f6' },
    { label: 'Mükemmel', max: 70, color: '#10b981' },
  ];
  
  return (
    <div className="space-y-3">
      {/* Bar chart */}
      <div className="relative h-8 bg-gray-100 rounded-full overflow-hidden flex">
        {ranges.map((range, i) => {
          const prevMax = i > 0 ? ranges[i-1].max : 0;
          const width = ((range.max - prevMax) / 70) * 100;
          return (
            <div
              key={range.label}
              className="h-full"
              style={{ width: `${width}%`, backgroundColor: range.color, opacity: 0.3 }}
            />
          );
        })}
        
        {/* Mevcut değer işaretçisi */}
        <div
          className="absolute top-0 h-full w-1 bg-gray-900"
          style={{ left: `${(efficiency / 70) * 100}%` }}
        />
      </div>
      
      {/* Lejant */}
      <div className="flex justify-between text-xs text-gray-500">
        <span>0%</span>
        <span>30%</span>
        <span>45%</span>
        <span>55%</span>
        <span>70%</span>
      </div>
      
      {/* Percentile */}
      <div className="text-center text-sm">
        <span className="text-gray-600">Sektör sıralaması: </span>
        <span className="font-semibold">İlk %{100 - percentile}</span>
      </div>
    </div>
  );
};
```

### 3.8 Çözüm Önerileri

#### SolutionsList.jsx

```jsx
const SolutionsList = ({ solutions }) => {
  if (!solutions || solutions.length === 0) return null;
  
  return (
    <div className="space-y-4">
      <h3 className="text-lg font-semibold text-gray-900">İyileştirme Önerileri</h3>
      
      {solutions.map((solution) => (
        <div
          key={solution.id}
          className="bg-white border border-gray-200 rounded-xl p-4 hover:shadow-md transition-shadow"
        >
          <div className="flex items-start justify-between">
            <div>
              <div className="flex items-center gap-2">
                <h4 className="font-medium text-gray-900">{solution.title}</h4>
                <PriorityBadge priority={solution.priority} />
              </div>
              <p className="text-sm text-gray-600 mt-1">{solution.description}</p>
            </div>
          </div>
          
          <div className="mt-4 grid grid-cols-3 gap-4 text-sm">
            <div>
              <span className="text-gray-500">Tasarruf Potansiyeli</span>
              <p className="font-semibold text-green-600">{solution.potential_savings_percent}%</p>
            </div>
            <div>
              <span className="text-gray-500">Tahmini Yatırım</span>
              <p className="font-semibold">{solution.estimated_investment_eur}</p>
            </div>
            <div>
              <span className="text-gray-500">Geri Ödeme</span>
              <p className="font-semibold">{solution.estimated_roi_years} yıl</p>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

const PriorityBadge = ({ priority }) => {
  const styles = {
    high: 'bg-red-100 text-red-700',
    medium: 'bg-amber-100 text-amber-700',
    low: 'bg-gray-100 text-gray-700',
  };
  
  const labels = {
    high: 'Yüksek Öncelik',
    medium: 'Orta Öncelik',
    low: 'Düşük Öncelik',
  };
  
  return (
    <span className={`px-2 py-0.5 rounded text-xs font-medium ${styles[priority]}`}>
      {labels[priority]}
    </span>
  );
};
```

---

## 🔌 BÖLÜM 4: API Entegrasyonu

### 4.1 API Service

#### services/api.js

```javascript
import axios from 'axios';

const API_BASE = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getCompressorTypes = async () => {
  const response = await api.get('/compressor-types');
  return response.data.types;
};

export const analyzeCompressor = async (compressorType, parameters) => {
  const response = await api.post('/analyze', {
    compressor_type: compressorType,
    parameters,
  });
  return response.data;
};

export const getBenchmarks = async (compressorType) => {
  const response = await api.get(`/benchmarks/${compressorType}`);
  return response.data;
};

export const getSolutions = async (compressorType, params) => {
  const response = await api.get(`/solutions/${compressorType}`, { params });
  return response.data;
};

export default api;
```

### 4.2 Custom Hooks

#### hooks/useCompressorTypes.js

```javascript
import { useState, useEffect } from 'react';
import { getCompressorTypes } from '../services/api';

export const useCompressorTypes = () => {
  const [types, setTypes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    const fetchTypes = async () => {
      try {
        const data = await getCompressorTypes();
        setTypes(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    
    fetchTypes();
  }, []);
  
  return { types, loading, error };
};
```

#### hooks/useAnalysis.js

```javascript
import { useState } from 'react';
import { analyzeCompressor, getSolutions } from '../services/api';

export const useAnalysis = () => {
  const [result, setResult] = useState(null);
  const [solutions, setSolutions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  
  const analyze = async (compressorType, parameters) => {
    setLoading(true);
    setError(null);
    
    try {
      // Analiz yap
      const analysisResult = await analyzeCompressor(compressorType, parameters);
      setResult(analysisResult.data);
      
      // Çözüm önerilerini al
      const solutionsResult = await getSolutions(compressorType, {
        efficiency: analysisResult.data.metrics.exergy_efficiency_percent,
        specific_power: parameters.power_kW / parameters.flow_rate_m3_min,
        operating_hours: parameters.operating_hours || 4000,
      });
      setSolutions(solutionsResult.recommendations);
      
    } catch (err) {
      setError(err.response?.data?.detail || err.message);
    } finally {
      setLoading(false);
    }
  };
  
  const reset = () => {
    setResult(null);
    setSolutions([]);
    setError(null);
  };
  
  return { result, solutions, loading, error, analyze, reset };
};
```

---

## 📱 BÖLÜM 5: Ana Uygulama

### App.jsx

```jsx
import { useState } from 'react';
import Layout from './components/layout/Layout';
import CompressorTypeSelector from './components/forms/CompressorTypeSelector';
import ParameterForm from './components/forms/ParameterForm';
import ResultsPanel from './components/results/ResultsPanel';
import SolutionsList from './components/results/SolutionsList';
import Card from './components/common/Card';
import { useCompressorTypes } from './hooks/useCompressorTypes';
import { useAnalysis } from './hooks/useAnalysis';

function App() {
  const { types, loading: typesLoading } = useCompressorTypes();
  const { result, solutions, loading, error, analyze, reset } = useAnalysis();
  
  const [selectedType, setSelectedType] = useState(null);
  const [formValues, setFormValues] = useState({});
  
  const selectedTypeData = types.find(t => t.id === selectedType);
  
  const handleTypeSelect = (typeId) => {
    setSelectedType(typeId);
    setFormValues({});
    reset();
  };
  
  const handleFormChange = (fieldId, value) => {
    setFormValues(prev => ({ ...prev, [fieldId]: value }));
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    analyze(selectedType, formValues);
  };
  
  return (
    <Layout>
      <div className="space-y-8">
        {/* Başlık */}
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Kompresör Exergy Analizi</h2>
          <p className="text-gray-600 mt-1">
            Kompresör tipini seçin ve parametreleri girin
          </p>
        </div>
        
        {/* Kompresör Tipi Seçimi */}
        <Card title="1. Kompresör Tipi">
          {typesLoading ? (
            <div className="h-32 flex items-center justify-center">
              <LoadingSpinner />
            </div>
          ) : (
            <CompressorTypeSelector
              types={types}
              selected={selectedType}
              onSelect={handleTypeSelect}
            />
          )}
        </Card>
        
        {/* Parametre Formu */}
        {selectedTypeData && (
          <Card title="2. Parametreler">
            <ParameterForm
              fields={selectedTypeData.fields}
              values={formValues}
              onChange={handleFormChange}
              onSubmit={handleSubmit}
              loading={loading}
            />
          </Card>
        )}
        
        {/* Hata Mesajı */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700">
            {error}
          </div>
        )}
        
        {/* Sonuçlar */}
        {result && (
          <>
            <div className="border-t border-gray-200 pt-8">
              <h2 className="text-2xl font-bold text-gray-900 mb-6">Analiz Sonuçları</h2>
              <ResultsPanel data={result} />
            </div>
            
            {solutions.length > 0 && (
              <SolutionsList solutions={solutions} />
            )}
          </>
        )}
      </div>
    </Layout>
  );
}

export default App;
```

---

## 🚀 BÖLÜM 6: Çalıştırma

```bash
cd exergy-lab/frontend
npm install
npm run dev
```

Açılacak adres: http://localhost:5173

**Not:** Backend'in çalışıyor olması gerekiyor (http://localhost:8000)

---

## ✅ Tamamlama Kontrol Listesi

Frontend tamamlandığında:

- [ ] Proje kurulumu (Vite + React + Tailwind)
- [ ] Layout components (Header, Footer)
- [ ] Kompresör tipi seçici çalışıyor
- [ ] Dinamik parametre formu çalışıyor
- [ ] API entegrasyonu çalışıyor
- [ ] Sonuç kartları görünüyor
- [ ] Sankey diyagramı görünüyor (Plotly)
- [ ] Benchmark grafiği görünüyor
- [ ] Çözüm önerileri listeleniyor
- [ ] Responsive tasarım (mobile uyumlu)
- [ ] Loading ve error state'leri

**Test:**
1. Backend'i başlat: `uvicorn api.main:app --reload --port 8000`
2. Frontend'i başlat: `cd frontend && npm run dev`
3. Tarayıcıda http://localhost:5173 aç
4. Vidalı kompresör seç, parametreleri gir, "Exergy Analizi Yap" tıkla
5. Sonuçları ve Sankey diyagramını gör

---

**Bu brief frontend geliştirme için tek kaynak noktasıdır.**
