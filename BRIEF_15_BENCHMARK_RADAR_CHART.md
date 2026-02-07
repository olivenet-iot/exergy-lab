# Brief 15: Benchmark Radar Chart — Çok Boyutlu Performans Görselleştirme

> **Claude Code için:** Bu brief'i oku ve uygula. Quick win — mevcut analiz verisinden radar chart üret. Yeni hesaplama yok, sadece mevcut metriklerin 0-100 skorlara dönüştürülmesi.

---

## 🎯 Hedef

Her ekipman analizi sonucunda **6 boyutlu radar chart** göster. Ekipmanın güçlü/zayıf yönlerini tek bakışta görebilmek. LinkedIn'e koyulabilir, sunum slide'ına yapıştırılabilir, müşteriye "bakın burada kötüsünüz" denilebilir.

**Effort:** Düşük. Yeni termodinamik hesap yok. Mevcut metriklerden skor türetme + Recharts RadarChart component.

---

## ⚠️ OTONOM YETKİ

1. Brief'teki görevleri tamamla
2. Mevcut frontend pattern'ı ve bileşenleri önce oku
3. Recharts'ın mevcut projede nasıl kullanıldığını incele (react-plotly.js mi kullanılıyor yoksa Recharts mı?)
4. Mevcut 374 testi BOZMA
5. Eksik gördüğün UX iyileştirmesi ekle

---

## 📋 Adım 0: ÖNCE Mevcut Kodu Anla

```bash
# 1. Frontend'de hangi grafik kütüphanesi kullanılıyor?
cat frontend/package.json | grep -i "chart\|plotly\|recharts\|d3"
grep -rn "recharts\|Plotly\|plotly\|RadarChart\|BarChart\|LineChart" frontend/src/

# 2. Mevcut BenchmarkChart component'i ne yapıyor?
cat frontend/src/components/results/BenchmarkChart.jsx

# 3. ResultsPanel'in yapısı
cat frontend/src/components/results/ResultsPanel.jsx

# 4. Mevcut analiz response'undan hangi metrikler dönüyor?
cat frontend/src/services/api.js | grep -A 5 "metrics\."

# 5. Backend'den dönen tüm metric field'lar
python3 -c "
from engine.compressor import CompressorInput, analyze_compressor
r = analyze_compressor(CompressorInput())
d = r.to_api_dict()
for k, v in d.items():
    print(f'{k}: {v}')
"

# 6. Aynısını boiler için — hangi field'lar var?
python3 -c "
from engine.boiler import BoilerInput, analyze_boiler
r = analyze_boiler(BoilerInput())
d = r.to_api_dict()
for k, v in d.items():
    print(f'{k}: {v}')
"
```

---

## 🧪 Radar Chart Boyutları (6 Eksen)

Tüm 7 ekipman tipi için **aynı 6 eksen**. Her eksen 0-100 arası skor. Yüksek = iyi.

### Eksen 1: Exergy Verimi
```
Skor = exergy_efficiency_pct
Doğrudan kullan — zaten 0-100 aralığında.
```

### Eksen 2: İyileştirme Durumu (AV/UN)
```
Skor = 100 - avoidable_ratio_pct
Düşük avoidable = ekipman zaten iyi optimize edilmiş = yüksek skor.
Yüksek avoidable = çok iyileştirme potansiyeli var = düşük skor.
```

### Eksen 3: Sektör Sıralaması
```
Mevcut benchmark_comparison string'inden percentile çıkar.
"İlk %7" → skor = 93
"İlk %25" → skor = 75
"İlk %50" → skor = 50
Benchmark string'i yoksa → skor = 50 (ortalama varsay)

Alternatif: Eğer benchmark_comparison bir percentile sayı değil de 
"Mükemmel/İyi/Orta/Kötü/Kritik" gibi label ise:
  Mükemmel → 95, İyi → 75, Orta → 50, Kötü → 25, Kritik → 10
```

### Eksen 4: Isı Geri Kazanım
```
recoverable_heat_kW / exergy_destroyed_kW × 100
Clamp: 0-100

Yoksa veya 0 ise → skor = 0 (geri kazanım potansiyeli yok/bilinmiyor)
Bazı ekipmanlarda (HX, steam turbine) bu field olmayabilir → equipment-specific fallback
```

### Eksen 5: Yıkım Oranı (ters)
```
Skor = 100 - (exergy_destroyed_kW / exergy_in_kW × 100)
Düşük yıkım oranı = yüksek skor.
Clamp: 0-100
```

### Eksen 6: Maliyet Etkinliği
```
Normalize: annual_loss_EUR bazlı skor
Yaklaşım: exergy_in_kW × operating_hours × energy_price = max_possible_cost
actual_annual_loss / max_possible_cost → loss_ratio
Skor = (1 - loss_ratio) × 100
Clamp: 0-100

Daha basit alternatif:
Skor = exergy_efficiency_pct ile korelasyonlu olacağından,
doğrudan 100 - (annual_loss_kWh / (exergy_in_kW × operating_hours) × 100) kullan.
```

---

## 📦 Adım 1: Backend — Radar Data Hesaplama

### 1.1 Yeni helper fonksiyon: `engine/radar.py`

Yeni bir dosya oluştur. Mevcut analiz verisini 6 boyutlu radar skoruna çevir.

```python
"""
ExergyLab - Benchmark Radar Chart Data Generator

Analiz sonuçlarını 6 boyutlu radar chart verisine dönüştürür.
Her eksen 0-100 arası. Yüksek = iyi performans.
"""

import re
from typing import Dict, List, Optional


# Radar eksenleri
RADAR_AXES = [
    {'key': 'exergy_efficiency', 'label': 'Exergy Verimi', 'label_en': 'Exergy Efficiency'},
    {'key': 'improvement_status', 'label': 'Optimizasyon Durumu', 'label_en': 'Optimization Status'},
    {'key': 'sector_ranking', 'label': 'Sektör Sıralaması', 'label_en': 'Sector Ranking'},
    {'key': 'heat_recovery', 'label': 'Isı Geri Kazanım', 'label_en': 'Heat Recovery'},
    {'key': 'destruction_ratio', 'label': 'Exergy Koruma', 'label_en': 'Exergy Preservation'},
    {'key': 'cost_efficiency', 'label': 'Maliyet Etkinliği', 'label_en': 'Cost Efficiency'},
]


def _clamp(value: float, min_val: float = 0.0, max_val: float = 100.0) -> float:
    """Değeri min-max aralığına sıkıştır"""
    return max(min_val, min(max_val, value))


def _parse_benchmark_score(benchmark_str: Optional[str]) -> float:
    """
    Benchmark comparison string'inden 0-100 skor çıkar.
    
    Örnekler:
      "İlk %7" → 93
      "İlk %25" → 75
      "Sektör sıralaması: İlk %7" → 93
      "Mükemmel" → 95
      "İyi" → 75
      "Orta" → 50
      "Kötü" / "Zayıf" → 25
      "Kritik" → 10
    """
    if not benchmark_str:
        return 50.0
    
    # Yüzdelik arama: "İlk %XX" veya "%XX"
    pct_match = re.search(r'[İi]lk\s*%\s*(\d+)', benchmark_str)
    if pct_match:
        percentile = int(pct_match.group(1))
        return _clamp(100 - percentile)
    
    # Label bazlı
    lower = benchmark_str.lower()
    if 'mükemmel' in lower or 'excellent' in lower:
        return 95.0
    elif 'iyi' in lower or 'good' in lower:
        return 75.0
    elif 'orta' in lower or 'average' in lower:
        return 50.0
    elif 'kötü' in lower or 'zayıf' in lower or 'poor' in lower:
        return 25.0
    elif 'kritik' in lower or 'critical' in lower:
        return 10.0
    
    return 50.0


def generate_radar_data(api_dict: dict) -> dict:
    """
    Analiz API dict'inden radar chart verisi üretir.
    
    Args:
        api_dict: to_api_dict() çıktısı veya API response metrics
    
    Returns:
        {
            'axes': [...],
            'scores': {'exergy_efficiency': 85.0, ...},
            'overall_score': 72.5,
            'grade': 'İyi',
            'grade_en': 'Good'
        }
    """
    scores = {}
    
    # 1. Exergy Verimi
    efficiency = api_dict.get('exergy_efficiency_pct', 0)
    scores['exergy_efficiency'] = _clamp(efficiency)
    
    # 2. Optimizasyon Durumu (100 - avoidable ratio)
    av_ratio = api_dict.get('avoidable_ratio_pct', 50)
    scores['improvement_status'] = _clamp(100 - av_ratio)
    
    # 3. Sektör Sıralaması
    benchmark = api_dict.get('benchmark_comparison', '')
    scores['sector_ranking'] = _parse_benchmark_score(benchmark)
    
    # 4. Isı Geri Kazanım
    destroyed = api_dict.get('exergy_destroyed_kW', 0) or 0
    recoverable = api_dict.get('recoverable_heat_kW', 0) or 0
    if destroyed > 0:
        recovery_pct = (recoverable / destroyed) * 100
        scores['heat_recovery'] = _clamp(recovery_pct)
    else:
        scores['heat_recovery'] = 50.0  # Yıkım yok = neutral
    
    # 5. Exergy Koruma (100 - yıkım oranı)
    exergy_in = api_dict.get('exergy_in_kW', 0) or 0
    if exergy_in > 0:
        destruction_ratio = (destroyed / exergy_in) * 100
        scores['destruction_ratio'] = _clamp(100 - destruction_ratio)
    else:
        scores['destruction_ratio'] = 50.0
    
    # 6. Maliyet Etkinliği
    annual_loss_kWh = api_dict.get('annual_loss_kWh', 0) or 0
    operating_hours = api_dict.get('operating_hours', 6000) or 6000
    if exergy_in > 0 and operating_hours > 0:
        max_possible_kWh = exergy_in * operating_hours
        loss_ratio = annual_loss_kWh / max_possible_kWh if max_possible_kWh > 0 else 0
        scores['cost_efficiency'] = _clamp((1 - loss_ratio) * 100)
    else:
        scores['cost_efficiency'] = 50.0
    
    # Overall skor (ortalama)
    overall = sum(scores.values()) / len(scores) if scores else 0
    
    # Grade
    if overall >= 85:
        grade, grade_en = 'Mükemmel', 'Excellent'
    elif overall >= 70:
        grade, grade_en = 'İyi', 'Good'
    elif overall >= 50:
        grade, grade_en = 'Orta', 'Average'
    elif overall >= 30:
        grade, grade_en = 'Zayıf', 'Poor'
    else:
        grade, grade_en = 'Kritik', 'Critical'
    
    return {
        'axes': RADAR_AXES,
        'scores': scores,
        'overall_score': round(overall, 1),
        'grade': grade,
        'grade_en': grade_en,
    }
```

### 1.2 Engine Entegrasyonu

**İki seçenek var. Mevcut koda en uygun olanı seç:**

**Seçenek A (Önerilen): API route'unda hesapla**

`api/routes/analysis.py`'de analyze endpoint'inin response'una `radar_data` ekle:

```python
from engine.radar import generate_radar_data

# Her _analyze_xxx() fonksiyonunda, response oluşturulduktan sonra:
radar = generate_radar_data(api_dict)
# Response'a ekle
```

**Seçenek B: Frontend'de hesapla**

Tüm gerekli metrikler zaten frontend'e dönüyor. Frontend'de bir utility fonksiyon ile radar skorları hesaplanabilir. Bu durumda backend'e dokunmaya gerek yok.

**Hangisi mevcut mimariye daha uygunsa onu seç.** Seçenek A daha clean (backend hesaplar, frontend sadece render eder). Seçenek B daha minimal (backend değişikliği yok).

### 1.3 API Response Güncelleme

Eğer Seçenek A ise, `api/schemas/responses.py`'ye ekle:

```python
# Yeni schema
class RadarScoreResponse(BaseModel):
    exergy_efficiency: float = 0
    improvement_status: float = 0
    sector_ranking: float = 0
    heat_recovery: float = 0
    destruction_ratio: float = 0
    cost_efficiency: float = 0

class RadarDataResponse(BaseModel):
    scores: RadarScoreResponse
    overall_score: float = 0
    grade: str = ''
    grade_en: str = ''

# AnalysisResponse'a ekle:
radar_data: Optional[RadarDataResponse] = None
```

### 1.4 `engine/__init__.py` güncelle

```python
from .radar import generate_radar_data, RADAR_AXES
```

---

## 📦 Adım 2: Frontend — Radar Chart Component

### 2.1 Grafik Kütüphanesi Tespiti

```bash
# Hangi grafik kütüphanesi var?
cat frontend/package.json | grep -i "chart\|plotly\|recharts"
```

**Senaryo 1: Recharts varsa** → `RadarChart` component'ini import et, doğrudan kullan.

**Senaryo 2: Sadece Plotly varsa** → Plotly'nin `scatterpolar` tipi ile radar chart yap.

**Senaryo 3: İkisi de yoksa** → Recharts ekle (`npm install recharts`) VEYA saf SVG/CSS ile yap.

### 2.2 Recharts ile RadarChart Component

Eğer Recharts mevcut veya eklenebilirse:

```jsx
// frontend/src/components/results/RadarBenchmark.jsx

import { RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar, ResponsiveContainer, Tooltip } from 'recharts';

const AXIS_LABELS = {
  exergy_efficiency: 'Exergy Verimi',
  improvement_status: 'Optimizasyon',
  sector_ranking: 'Sektör Sıralaması',
  heat_recovery: 'Isı Geri Kazanım',
  destruction_ratio: 'Exergy Koruma',
  cost_efficiency: 'Maliyet Etkinliği',
};

export default function RadarBenchmark({ radarData }) {
  if (!radarData?.scores) return null;

  const { scores, overall_score, grade } = radarData;

  // Recharts data format
  const chartData = Object.entries(AXIS_LABELS).map(([key, label]) => ({
    axis: label,
    value: scores[key] || 0,
    fullMark: 100,
  }));

  // Grade rengi
  const gradeColor = overall_score >= 85 ? 'text-green-600'
    : overall_score >= 70 ? 'text-blue-600'
    : overall_score >= 50 ? 'text-yellow-600'
    : overall_score >= 30 ? 'text-orange-600'
    : 'text-red-600';

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-sm font-semibold text-gray-700">
          Performans Radar
        </h3>
        <div className="text-right">
          <span className={`text-2xl font-bold ${gradeColor}`}>
            {overall_score}
          </span>
          <span className="text-sm text-gray-500 ml-1">/ 100</span>
          <div className={`text-xs font-medium ${gradeColor}`}>{grade}</div>
        </div>
      </div>

      <ResponsiveContainer width="100%" height={300}>
        <RadarChart data={chartData}>
          <PolarGrid stroke="#e5e7eb" />
          <PolarAngleAxis
            dataKey="axis"
            tick={{ fontSize: 11, fill: '#6b7280' }}
          />
          <PolarRadiusAxis
            angle={90}
            domain={[0, 100]}
            tick={{ fontSize: 10 }}
            tickCount={5}
          />
          <Radar
            name="Performans"
            dataKey="value"
            stroke="#3b82f6"
            fill="#3b82f6"
            fillOpacity={0.2}
            strokeWidth={2}
          />
          <Tooltip
            formatter={(value) => [`${value.toFixed(0)}`, 'Skor']}
          />
        </RadarChart>
      </ResponsiveContainer>

      {/* Eksen açıklamaları */}
      <div className="grid grid-cols-3 gap-2 mt-3 text-xs text-gray-500">
        {chartData.map(item => (
          <div key={item.axis} className="flex items-center gap-1">
            <div className={`w-2 h-2 rounded-full ${
              item.value >= 70 ? 'bg-green-400' : item.value >= 40 ? 'bg-yellow-400' : 'bg-red-400'
            }`} />
            <span>{item.axis}: {item.value.toFixed(0)}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
```

### 2.3 Plotly ile Radar Chart (Alternatif)

Eğer projede sadece Plotly varsa:

```jsx
// frontend/src/components/results/RadarBenchmark.jsx

import Plot from 'react-plotly.js';

const AXIS_LABELS = {
  exergy_efficiency: 'Exergy Verimi',
  improvement_status: 'Optimizasyon',
  sector_ranking: 'Sektör Sıralaması',
  heat_recovery: 'Isı Geri Kazanım',
  destruction_ratio: 'Exergy Koruma',
  cost_efficiency: 'Maliyet Etkinliği',
};

export default function RadarBenchmark({ radarData }) {
  if (!radarData?.scores) return null;

  const { scores, overall_score, grade } = radarData;

  const labels = Object.values(AXIS_LABELS);
  const values = Object.keys(AXIS_LABELS).map(key => scores[key] || 0);

  // Plotly radar: kapatmak için ilk noktayı sona ekle
  const r = [...values, values[0]];
  const theta = [...labels, labels[0]];

  const gradeColor = overall_score >= 85 ? 'text-green-600'
    : overall_score >= 70 ? 'text-blue-600'
    : overall_score >= 50 ? 'text-yellow-600'
    : overall_score >= 30 ? 'text-orange-600'
    : 'text-red-600';

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4">
      <div className="flex items-center justify-between mb-2">
        <h3 className="text-sm font-semibold text-gray-700">Performans Radar</h3>
        <div className="text-right">
          <span className={`text-2xl font-bold ${gradeColor}`}>{overall_score}</span>
          <span className="text-sm text-gray-500 ml-1">/ 100</span>
          <div className={`text-xs font-medium ${gradeColor}`}>{grade}</div>
        </div>
      </div>

      <Plot
        data={[{
          type: 'scatterpolar',
          r: r,
          theta: theta,
          fill: 'toself',
          fillcolor: 'rgba(59, 130, 246, 0.15)',
          line: { color: '#3b82f6', width: 2 },
          marker: { size: 6, color: '#3b82f6' },
          name: 'Performans',
        }]}
        layout={{
          polar: {
            radialaxis: {
              visible: true,
              range: [0, 100],
              tickfont: { size: 10 },
            },
            angularaxis: {
              tickfont: { size: 11 },
            },
          },
          showlegend: false,
          margin: { t: 30, b: 30, l: 60, r: 60 },
          height: 320,
          paper_bgcolor: 'transparent',
          plot_bgcolor: 'transparent',
        }}
        config={{ displayModeBar: false, responsive: true }}
        style={{ width: '100%' }}
      />
    </div>
  );
}
```

### 2.4 ResultsPanel'e Entegrasyon

```jsx
// ResultsPanel.jsx'e import ekle:
import RadarBenchmark from './RadarBenchmark';

// Uygun yere ekle (BenchmarkChart'ın yanına veya altına):
{radarData && <RadarBenchmark radarData={radarData} />}
```

### 2.5 API Service'de Radar Data Mapping

```javascript
// api.js — analyzeEquipment/analyzeCompressor return'e ekle:
radar_data: data.radar_data || null,
```

---

## 📦 Adım 3: Factory Dashboard — Çoklu Radar

Factory analizi sonuçlarında birden fazla ekipman varsa, hepsinin radar'larını yan yana veya overlay olarak göster.

### 3.1 Overlay Radar (Tek Grafik, Birden Fazla Ekipman)

Factory dashboard'da tüm ekipmanların radar'larını üst üste çiz:

```jsx
// Her ekipman farklı renkte:
const EQUIPMENT_COLORS = {
  compressor: '#3b82f6',  // mavi
  boiler: '#ef4444',      // kırmızı
  chiller: '#06b6d4',     // cyan
  pump: '#8b5cf6',        // mor
  heat_exchanger: '#a855f7', // purple
  steam_turbine: '#eab308', // sarı
  dryer: '#f97316',       // turuncu
};
```

Bu bölüm opsiyonel — tek ekipman radar'ı priority.

---

## 📦 Adım 4: Testler

### 4.1 `tests/test_radar.py`

```python
"""Radar chart data generation testleri"""
import pytest
from engine.radar import generate_radar_data, _parse_benchmark_score, _clamp


class TestClamp:
    def test_within_range(self):
        assert _clamp(50) == 50

    def test_below_min(self):
        assert _clamp(-10) == 0

    def test_above_max(self):
        assert _clamp(150) == 100


class TestParseBenchmark:
    def test_ilk_yuzde(self):
        assert _parse_benchmark_score("İlk %7") == 93

    def test_ilk_yuzde_with_context(self):
        assert _parse_benchmark_score("Sektör sıralaması: İlk %25") == 75

    def test_mukemmel(self):
        assert _parse_benchmark_score("Mükemmel") == 95

    def test_iyi(self):
        assert _parse_benchmark_score("İyi") == 75

    def test_orta(self):
        assert _parse_benchmark_score("Orta") == 50

    def test_kotu(self):
        assert _parse_benchmark_score("Kötü") == 25

    def test_kritik(self):
        assert _parse_benchmark_score("Kritik") == 10

    def test_none(self):
        assert _parse_benchmark_score(None) == 50

    def test_empty(self):
        assert _parse_benchmark_score("") == 50


class TestGenerateRadarData:
    def test_basic_structure(self):
        data = generate_radar_data({
            'exergy_efficiency_pct': 75,
            'avoidable_ratio_pct': 30,
            'benchmark_comparison': 'İlk %20',
            'exergy_destroyed_kW': 10,
            'recoverable_heat_kW': 5,
            'exergy_in_kW': 100,
            'annual_loss_kWh': 50000,
            'operating_hours': 6000,
        })
        assert 'axes' in data
        assert 'scores' in data
        assert 'overall_score' in data
        assert 'grade' in data
        assert len(data['scores']) == 6

    def test_all_scores_in_range(self):
        data = generate_radar_data({
            'exergy_efficiency_pct': 75,
            'avoidable_ratio_pct': 30,
        })
        for key, score in data['scores'].items():
            assert 0 <= score <= 100, f'{key} = {score} out of range'

    def test_high_performance_grade(self):
        data = generate_radar_data({
            'exergy_efficiency_pct': 92,
            'avoidable_ratio_pct': 10,
            'benchmark_comparison': 'Mükemmel',
            'exergy_destroyed_kW': 5,
            'recoverable_heat_kW': 4,
            'exergy_in_kW': 100,
            'annual_loss_kWh': 5000,
            'operating_hours': 6000,
        })
        assert data['overall_score'] > 70
        assert data['grade'] in ('Mükemmel', 'İyi')

    def test_low_performance_grade(self):
        data = generate_radar_data({
            'exergy_efficiency_pct': 20,
            'avoidable_ratio_pct': 80,
            'benchmark_comparison': 'Kritik',
            'exergy_destroyed_kW': 80,
            'recoverable_heat_kW': 5,
            'exergy_in_kW': 100,
            'annual_loss_kWh': 400000,
            'operating_hours': 6000,
        })
        assert data['overall_score'] < 50
        assert data['grade'] in ('Zayıf', 'Kritik')

    def test_empty_input(self):
        """Boş dict ile crash olmamalı"""
        data = generate_radar_data({})
        assert data['overall_score'] >= 0
        assert len(data['scores']) == 6

    def test_all_engines_produce_radar(self):
        """7 engine'in hepsi radar data üretebilmeli"""
        from engine.compressor import CompressorInput, analyze_compressor
        from engine.boiler import BoilerInput, analyze_boiler
        from engine.chiller import ChillerInput, analyze_chiller
        from engine.pump import PumpInput, analyze_pump
        from engine.heat_exchanger import HeatExchangerInput, analyze_heat_exchanger
        from engine.steam_turbine import SteamTurbineInput, analyze_steam_turbine
        from engine.dryer import DryerInput, analyze_dryer

        engines = [
            ('compressor', CompressorInput(), analyze_compressor),
            ('boiler', BoilerInput(), analyze_boiler),
            ('chiller', ChillerInput(), analyze_chiller),
            ('pump', PumpInput(), analyze_pump),
            ('heat_exchanger', HeatExchangerInput(), analyze_heat_exchanger),
            ('steam_turbine', SteamTurbineInput(), analyze_steam_turbine),
            ('dryer', DryerInput(), analyze_dryer),
        ]

        for name, inp, func in engines:
            result = func(inp)
            api_dict = result.to_api_dict()
            radar = generate_radar_data(api_dict)
            assert len(radar['scores']) == 6, f'{name} radar has {len(radar["scores"])} scores'
            assert 0 <= radar['overall_score'] <= 100, f'{name} overall={radar["overall_score"]}'
            print(f'✅ {name}: overall={radar["overall_score"]:.0f} grade={radar["grade"]}')
```

---

## 📋 Entegrasyon Doğrulama

```bash
# 1. Radar modülü çalışıyor
python3 -c "
from engine.radar import generate_radar_data
from engine.compressor import CompressorInput, analyze_compressor
r = analyze_compressor(CompressorInput())
radar = generate_radar_data(r.to_api_dict())
print(f'Overall: {radar[\"overall_score\"]}, Grade: {radar[\"grade\"]}')
for k, v in radar['scores'].items():
    print(f'  {k}: {v:.0f}')
"

# 2. Tüm engine'ler
python3 -c "
from engine.radar import generate_radar_data
from engine.compressor import CompressorInput, analyze_compressor
from engine.boiler import BoilerInput, analyze_boiler
from engine.chiller import ChillerInput, analyze_chiller
from engine.pump import PumpInput, analyze_pump
from engine.heat_exchanger import HeatExchangerInput, analyze_heat_exchanger
from engine.steam_turbine import SteamTurbineInput, analyze_steam_turbine
from engine.dryer import DryerInput, analyze_dryer

for name, inp, func in [
    ('Compressor', CompressorInput(), analyze_compressor),
    ('Boiler', BoilerInput(), analyze_boiler),
    ('Chiller', ChillerInput(), analyze_chiller),
    ('Pump', PumpInput(), analyze_pump),
    ('HeatExchanger', HeatExchangerInput(), analyze_heat_exchanger),
    ('SteamTurbine', SteamTurbineInput(), analyze_steam_turbine),
    ('Dryer', DryerInput(), analyze_dryer),
]:
    r = func(inp)
    radar = generate_radar_data(r.to_api_dict())
    scores = ' | '.join(f'{k[:3]}={v:.0f}' for k, v in radar['scores'].items())
    print(f'✅ {name:15s} → {radar[\"overall_score\"]:5.1f} ({radar[\"grade\"]}) | {scores}')
"

# 3. API endpoint testi
python3 -c "
from fastapi.testclient import TestClient
from api.main import app
client = TestClient(app)
resp = client.post('/api/analyze', json={
    'equipment_type': 'compressor',
    'subtype': 'screw',
    'params': {}
})
data = resp.json()
assert 'radar_data' in data, f'radar_data missing from response. Keys: {list(data.keys())}'
print(f'✅ API returns radar_data: {data[\"radar_data\"][\"overall_score\"]} ({data[\"radar_data\"][\"grade\"]})')
"

# 4. Frontend build
cd frontend && npx vite build 2>&1 | tail -5

# 5. Backend testler
cd .. && pytest tests/ -v | tail -20
```

---

## ⚠️ Dikkat Edilecekler

1. **Grafik kütüphanesi:** Projede `plotly.js` + `react-plotly.js` var. Recharts YOK. Bu yüzden Plotly `scatterpolar` kullan veya saf CSS/SVG ile yap. **Yeni npm paketi ekleme** zorunlu değilse ekleme.

2. **Benchmark string parsing:** Mevcut benchmark_comparison field'ı her engine'de farklı format olabilir. `_parse_benchmark_score()` fonksiyonu defensive olmalı.

3. **Missing fields:** Bazı engine'lerde `recoverable_heat_kW` olmayabilir. `api_dict.get(key, 0) or 0` pattern'ını kullan (None guard).

4. **Factory radar overlay:** Bu opsiyonel. Tek ekipman radar'ı priority. Factory overlay sonra eklenebilir.

5. **Responsive:** Mobile'da radar chart küçük ekranda okunabilir olmalı. Height'ı 280-320px arası tut.

---

## ✅ Tamamlanma Kriterleri

- [ ] `engine/radar.py` oluşturuldu — `generate_radar_data()` fonksiyonu çalışıyor
- [ ] `engine/__init__.py` güncellendi — radar export
- [ ] 7 engine'in hepsi radar data üretebiliyor
- [ ] API response'a `radar_data` eklendi
- [ ] Frontend'de RadarBenchmark component oluşturuldu
- [ ] ResultsPanel'e RadarBenchmark entegre edildi
- [ ] Mevcut 374 test hâlâ geçiyor
- [ ] Yeni testler (~12) geçiyor
- [ ] Frontend build başarılı
- [ ] `git add -A && git commit && git push`

---

## 📊 Beklenen Sonuç

| Metrik | Önceki | Sonrası |
|--------|--------|---------|
| Radar chart | Yok | 7/7 ekipman |
| Overall grade | Yok | Mükemmel/İyi/Orta/Zayıf/Kritik |
| Görsel boyut | Sankey + bar | Sankey + bar + radar |
| Test sayısı | 374 | ~386 |
