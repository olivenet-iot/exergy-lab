# ExergyLab AI Entegrasyonu Brief (Claude Code)

> **Claude Code için:** Bu dosyayı oku, ExergyLab'a Claude Code tabanlı AI yorumlama entegrasyonu ekle.

---

## 🎯 Görev Özeti

Exergy analiz sonuçlarını **Claude Code** kullanarak yorumlat. Harici API key gereksiz — Claude Code zaten proje dizininde çalışıyor ve tüm knowledge base'e erişimi var.

**Mimari:**
```
Frontend → Backend (FastAPI) → Claude Code CLI → Yanıt
                                    ↓
                              /knowledge/*.md (benchmark, çözümler, metodoloji)
```

---

## 📁 Oluşturulacak/Güncellenecek Dosyalar

```
exergy-lab/
├── skills/
│   └── SKILL_exergy_interpreter.md  # YENİ: Claude Code yorumlama skill'i
├── api/
│   ├── main.py                      # Güncelle: /api/interpret endpoint
│   ├── routes/
│   │   └── interpret.py             # YENİ: Claude Code çağrısı
│   └── services/
│       └── claude_code_service.py   # YENİ: Claude Code CLI wrapper
└── frontend/
    └── src/
        ├── services/api.js          # Güncelle: interpretAnalysis
        ├── hooks/useAnalysis.js     # Güncelle: AI state
        ├── components/results/
        │   └── AIInterpretation.jsx # YENİ: AI yorum component
        └── App.jsx                  # Güncelle: AI component ekle
```

---

## 🧠 BÖLÜM 1: Claude Code Skill Dosyası

Bu skill, Claude Code'a exergy sonuçlarını nasıl yorumlayacağını öğretir.

### `/skills/SKILL_exergy_interpreter.md`:

```markdown
# SKILL: Exergy Analiz Yorumlayıcı

## Bu skill ne yapar?

Kompresör exergy analizi sonuçlarını yorumlar ve işletmeye özgü öneriler üretir.

## Ne zaman kullanılır?

- Kullanıcı exergy analiz sonuçlarını yorumlatmak istediğinde
- "Bu sonuçları yorumla", "Analizi değerlendir" gibi isteklerde
- Backend /api/interpret endpoint'i çağrıldığında

## Bilgi Kaynakları

Yorumlama yaparken şu dosyaları referans al:

1. **Benchmark verileri:** `/knowledge/benchmarks/compressor_benchmarks.md`
   - Exergy verimi aralıkları (düşük/ortalama/iyi/mükemmel)
   - Spesifik güç tüketimi referansları
   - Sektörel karşılaştırmalar

2. **Çözüm önerileri:** `/knowledge/solutions/`
   - `compressor_vsd.md` — Değişken hız sürücü
   - `compressor_air_leaks.md` — Kaçak tespiti
   - `compressor_pressure_optimization.md` — Basınç optimizasyonu
   - `compressor_heat_recovery.md` — Isı geri kazanımı
   - `compressor_maintenance.md` — Bakım iyileştirmeleri
   - `compressor_dryer_optimization.md` — Kurutucu optimizasyonu

3. **Ekipman bilgisi:** `/knowledge/equipment/`
   - Kompresör tiplerine özgü karakteristikler
   - Tipik verimlilik aralıkları

## Yorumlama Kuralları

1. **Bağlama göre öneri:** 
   - Exergy verimi zaten yüksekse (>55%) VSD önerme
   - Düşük çalışma saatinde (<3000) büyük yatırım önerme
   - Yük faktörü sabit ise VSD önerme

2. **Önceliklendirme:**
   - Hızlı ROI (<1 yıl): Yüksek öncelik
   - Orta ROI (1-3 yıl): Orta öncelik
   - Uzun ROI (>3 yıl): Düşük öncelik

3. **Somut rakamlar:**
   - Her öneride tahmini tasarruf €/yıl
   - Geri ödeme süresi
   - Yatırım maliyeti aralığı

4. **Eleme kriterleri:**
   - Uygulanamaz önerileri listele ama neden uygulanamaz açıkla
   - Mevcut duruma uygun olmayanları çıkar

## Çıktı Formatı

JSON formatında yanıt ver:

```json
{
  "summary": "2-3 cümlelik özet",
  "detailed_analysis": "Detaylı analiz (5-7 cümle)",
  "efficiency_assessment": {
    "rating": "excellent/good/average/poor",
    "comparison": "Sektör ortalamasına göre...",
    "percentile": 75
  },
  "key_insights": [
    "Bulgu 1",
    "Bulgu 2"
  ],
  "prioritized_recommendations": [
    {
      "id": "vsd_retrofit",
      "title": "Öneri başlığı",
      "priority": "high/medium/low",
      "applicable": true,
      "reason": "Neden bu öneri uygun",
      "expected_savings_eur": 2500,
      "investment_eur": "4000-8000",
      "payback_years": 2.5,
      "first_action": "Yapılacak ilk adım"
    }
  ],
  "not_recommended": [
    {
      "id": "heat_recovery",
      "title": "Isı geri kazanımı",
      "reason": "Mevsimsel kullanım faktörü düşük, ROI 5+ yıl"
    }
  ],
  "action_plan": {
    "immediate": ["Hemen yapılacak (0-1 ay)"],
    "short_term": ["Kısa vade (1-6 ay)"],
    "medium_term": ["Orta vade (6-12 ay)"]
  },
  "warnings": ["Dikkat edilmesi gerekenler"]
}
```

## Örnek Yorumlama

**Girdi:**
- Kompresör: Vidalı, 32 kW
- Exergy verimi: %45
- Yıllık çalışma: 6000 saat
- Benchmark: Ortalama

**Çıktı:**
```json
{
  "summary": "Kompresör exergy verimi %45 ile sektör ortalamasında. Yıllık 6000 saat çalışma ve €8000 enerji kaybı göz önüne alındığında, VSD retrofit ve kaçak giderme ile yılda €3500+ tasarruf potansiyeli var.",
  "detailed_analysis": "32 kW vidalı kompresör %45 exergy verimi ile çalışıyor. Bu değer sektör ortalaması olan %35-45 bandının üst sınırında. Ancak yıllık 80,000 kWh kayıp ve €8000 maliyet önemli bir iyileştirme potansiyeline işaret ediyor. Yük profili değişken olduğundan VSD retrofit en yüksek tasarrufu sağlayacaktır. Kaçak taraması yapılmamışsa, tipik %20-25 kaçak oranı ile hızlı kazanım mümkün.",
  "prioritized_recommendations": [
    {
      "id": "leak_detection",
      "title": "Kaçak Tespiti ve Giderme",
      "priority": "high",
      "applicable": true,
      "reason": "Düşük yatırım, hızlı ROI. Tipik tesiste %20-25 kaçak.",
      "expected_savings_eur": 1600,
      "investment_eur": "500-2000",
      "payback_years": 0.5,
      "first_action": "Ultrasonik kaçak taraması yaptır"
    }
  ]
}
```
```

---

## 🔧 BÖLÜM 2: Backend - Claude Code Servisi

### `/api/services/claude_code_service.py`:

```python
import subprocess
import json
import os
from pathlib import Path

# Proje kök dizini
PROJECT_ROOT = Path(__file__).parent.parent.parent

async def interpret_with_claude_code(
    analysis_result: dict,
    compressor_type: str,
    parameters: dict
) -> dict:
    """
    Claude Code CLI kullanarak exergy sonuçlarını yorumlat.
    
    Claude Code proje dizininde çalışır ve /knowledge/*.md dosyalarına erişir.
    """
    
    # Prompt oluştur
    prompt = _build_interpretation_prompt(analysis_result, compressor_type, parameters)
    
    try:
        # Claude Code CLI çağrısı
        result = subprocess.run(
            [
                "claude",
                "-p", str(PROJECT_ROOT),  # Proje dizini
                "--output-format", "json",
                "-m", prompt
            ],
            capture_output=True,
            text=True,
            timeout=60,  # 60 saniye timeout
            cwd=str(PROJECT_ROOT)
        )
        
        if result.returncode != 0:
            raise Exception(f"Claude Code error: {result.stderr}")
        
        # JSON yanıtı parse et
        response_text = result.stdout.strip()
        
        # JSON bloğunu çıkar
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0]
        elif "```" in response_text:
            parts = response_text.split("```")
            for part in parts:
                if part.strip().startswith("{"):
                    response_text = part
                    break
        
        return json.loads(response_text.strip())
        
    except subprocess.TimeoutExpired:
        return _fallback_response("Zaman aşımı - Claude Code yanıt vermedi")
    except json.JSONDecodeError as e:
        return _fallback_response(f"JSON parse hatası: {str(e)}")
    except FileNotFoundError:
        return _fallback_response("Claude Code CLI bulunamadı")
    except Exception as e:
        return _fallback_response(str(e))


def _build_interpretation_prompt(analysis_result: dict, compressor_type: str, parameters: dict) -> str:
    """Yorumlama promptu oluştur"""
    
    metrics = analysis_result.get('metrics', {})
    benchmark = analysis_result.get('benchmark', {})
    heat_recovery = analysis_result.get('heat_recovery', {})
    
    prompt = f"""Sen ExergyLab'ın AI yorumlayıcısısın. /skills/SKILL_exergy_interpreter.md dosyasını oku ve talimatları uygula.

Aşağıdaki kompresör exergy analiz sonuçlarını yorumla:

## Kompresör Bilgileri
- Tip: {compressor_type}
- Elektrik Gücü: {parameters.get('power_kW', 'N/A')} kW
- Hava Debisi: {parameters.get('flow_rate_m3_min', 'N/A')} m³/min
- Çıkış Basıncı: {parameters.get('outlet_pressure_bar', 'N/A')} bar
- Yıllık Çalışma: {parameters.get('operating_hours', 4000)} saat
- Yük Faktörü: {parameters.get('load_factor', 0.75)}
- Elektrik Fiyatı: {parameters.get('electricity_price', 0.10)} €/kWh

## Analiz Sonuçları
- Exergy Verimi: {metrics.get('exergy_efficiency_percent', 0):.1f}%
- Exergy Girişi: {metrics.get('exergy_input_kW', 0):.1f} kW
- Faydalı Exergy: {metrics.get('exergy_output_kW', 0):.1f} kW
- Exergy Yıkımı: {metrics.get('exergy_destroyed_kW', 0):.1f} kW
- Yıllık Enerji Kaybı: {metrics.get('annual_loss_kWh', 0):,.0f} kWh
- Yıllık Maliyet: €{metrics.get('annual_cost_eur', 0):,.0f}
- Benchmark Sıralaması: {benchmark.get('rating', 'N/A')}
- Isı Geri Kazanım Potansiyeli: {heat_recovery.get('potential_kW', 0):.1f} kW

## Görev
1. /knowledge/benchmarks/compressor_benchmarks.md dosyasını oku
2. /knowledge/solutions/ altındaki ilgili çözüm dosyalarını tara
3. Sonuçları yorumla ve JSON formatında yanıt ver

Sadece JSON yanıt ver, başka açıklama ekleme. SKILL dosyasındaki formata uy."""

    return prompt


def _fallback_response(error_message: str) -> dict:
    """Claude Code başarısız olursa fallback yanıt"""
    return {
        "summary": "AI yorumlama şu an kullanılamıyor.",
        "detailed_analysis": "",
        "efficiency_assessment": {
            "rating": "unknown",
            "comparison": "",
            "percentile": 0
        },
        "key_insights": [],
        "prioritized_recommendations": [],
        "not_recommended": [],
        "action_plan": {
            "immediate": [],
            "short_term": [],
            "medium_term": []
        },
        "warnings": [f"AI servisi hatası: {error_message}"],
        "ai_available": False
    }
```

---

## 🌐 BÖLÜM 3: API Endpoint

### `/api/routes/interpret.py`:

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
from api.services.claude_code_service import interpret_with_claude_code

router = APIRouter()

class InterpretRequest(BaseModel):
    analysis_result: Dict[str, Any]
    compressor_type: str
    parameters: Dict[str, Any]

class InterpretResponse(BaseModel):
    success: bool
    interpretation: Dict[str, Any]

@router.post("/interpret", response_model=InterpretResponse)
async def interpret_analysis(request: InterpretRequest):
    """
    Exergy analiz sonuçlarını Claude Code ile yorumla.
    
    Claude Code proje dizininde çalışır ve knowledge base'e erişir.
    """
    try:
        interpretation = await interpret_with_claude_code(
            analysis_result=request.analysis_result,
            compressor_type=request.compressor_type,
            parameters=request.parameters
        )
        
        return InterpretResponse(
            success=True,
            interpretation=interpretation
        )
        
    except Exception as e:
        # Hata olsa da fallback yanıt dön
        return InterpretResponse(
            success=False,
            interpretation={
                "summary": "Yorumlama yapılamadı",
                "warnings": [str(e)],
                "ai_available": False
            }
        )
```

### `/api/main.py` - Güncelle:

```python
# Mevcut importlara ekle:
from api.routes import analysis, benchmarks, solutions, interpret

# Mevcut router'lara ekle:
app.include_router(interpret.router, prefix="/api", tags=["AI Interpretation"])
```

---

## 🎨 BÖLÜM 4: Frontend

### `/frontend/src/services/api.js` - Ekle:

```javascript
export const interpretAnalysis = async (analysisResult, compressorType, parameters) => {
  const response = await api.post('/interpret', {
    analysis_result: analysisResult,
    compressor_type: compressorType,
    parameters: parameters
  });
  return response.data;
};
```

### `/frontend/src/hooks/useAnalysis.js` - Güncelle:

```javascript
import { useState } from 'react';
import { analyzeCompressor, getSolutions, interpretAnalysis } from '../services/api';

export const useAnalysis = () => {
  const [result, setResult] = useState(null);
  const [solutions, setSolutions] = useState([]);
  const [interpretation, setInterpretation] = useState(null);
  const [loading, setLoading] = useState(false);
  const [aiLoading, setAiLoading] = useState(false);
  const [error, setError] = useState(null);
  
  const analyze = async (compressorType, parameters) => {
    setLoading(true);
    setError(null);
    setInterpretation(null);
    
    try {
      // 1. Exergy hesaplama (hızlı)
      const analysisResult = await analyzeCompressor(compressorType, parameters);
      setResult(analysisResult);
      
      // 2. Statik çözüm önerileri (hızlı)
      const solutionsResult = await getSolutions(compressorType, {
        efficiency: analysisResult?.metrics?.exergy_efficiency_percent,
        specific_power: parameters.power_kW / parameters.flow_rate_m3_min,
        operating_hours: parameters.operating_hours || 4000,
      });
      setSolutions(solutionsResult.recommendations || []);
      
      setLoading(false);
      
      // 3. AI yorumlama (Claude Code - biraz daha yavaş)
      setAiLoading(true);
      try {
        const aiResult = await interpretAnalysis(analysisResult, compressorType, parameters);
        if (aiResult.success) {
          setInterpretation(aiResult.interpretation);
        }
      } catch (aiError) {
        console.error('AI interpretation failed:', aiError);
        // AI başarısız olsa da ana sonuçlar gösterilir
      }
      setAiLoading(false);
      
    } catch (err) {
      setError(err.response?.data?.detail || err.message);
      setLoading(false);
      setAiLoading(false);
    }
  };
  
  const reset = () => {
    setResult(null);
    setSolutions([]);
    setInterpretation(null);
    setError(null);
  };
  
  return { 
    result, 
    solutions, 
    interpretation, 
    loading, 
    aiLoading, 
    error, 
    analyze, 
    reset 
  };
};
```

### `/frontend/src/components/results/AIInterpretation.jsx`:

```jsx
import { Sparkles, AlertTriangle, CheckCircle, ArrowRight, XCircle } from 'lucide-react';
import Card from '../common/Card';

const AIInterpretation = ({ interpretation, loading }) => {
  if (loading) {
    return (
      <Card>
        <div className="flex items-center gap-3 text-primary-600">
          <Sparkles className="w-5 h-5 animate-pulse" />
          <span>Claude Code analiz yapıyor...</span>
        </div>
        <div className="mt-2 text-sm text-gray-500">
          Knowledge base taranıyor, öneriler önceliklendiriliyor...
        </div>
      </Card>
    );
  }
  
  if (!interpretation || interpretation.ai_available === false) {
    return null; // AI yoksa statik öneriler gösterilecek
  }
  
  const { 
    summary, 
    detailed_analysis,
    efficiency_assessment,
    key_insights, 
    prioritized_recommendations,
    not_recommended,
    action_plan, 
    warnings 
  } = interpretation;
  
  return (
    <div className="space-y-6">
      {/* AI Badge + Özet */}
      <Card>
        <div className="flex items-start gap-3">
          <div className="p-2 bg-primary-100 rounded-lg">
            <Sparkles className="w-5 h-5 text-primary-600" />
          </div>
          <div className="flex-1">
            <h3 className="font-semibold text-gray-900 flex items-center gap-2">
              AI Analizi
              <span className="text-xs bg-primary-100 text-primary-700 px-2 py-0.5 rounded">
                Claude Code
              </span>
            </h3>
            <p className="text-gray-700 mt-2">{summary}</p>
          </div>
        </div>
      </Card>
      
      {/* Detaylı Analiz */}
      {detailed_analysis && (
        <Card title="Detaylı Değerlendirme">
          <p className="text-gray-700 leading-relaxed">{detailed_analysis}</p>
          
          {efficiency_assessment && (
            <div className="mt-4 p-3 bg-gray-50 rounded-lg">
              <span className="text-sm text-gray-600">
                {efficiency_assessment.comparison}
              </span>
            </div>
          )}
        </Card>
      )}
      
      {/* Önemli Bulgular */}
      {key_insights && key_insights.length > 0 && (
        <Card title="Önemli Bulgular">
          <ul className="space-y-2">
            {key_insights.map((insight, i) => (
              <li key={i} className="flex items-start gap-2">
                <CheckCircle className="w-5 h-5 text-green-500 shrink-0 mt-0.5" />
                <span className="text-gray-700">{insight}</span>
              </li>
            ))}
          </ul>
        </Card>
      )}
      
      {/* Önceliklendirilmiş Öneriler */}
      {prioritized_recommendations && prioritized_recommendations.length > 0 && (
        <Card title="Öncelikli Aksiyon Planı">
          <div className="space-y-4">
            {prioritized_recommendations.filter(r => r.applicable !== false).map((rec, i) => (
              <div 
                key={i}
                className={`p-4 rounded-lg border-l-4 ${
                  rec.priority === 'high' 
                    ? 'bg-red-50 border-red-500' 
                    : rec.priority === 'medium'
                    ? 'bg-amber-50 border-amber-500'
                    : 'bg-gray-50 border-gray-300'
                }`}
              >
                <div className="flex items-center justify-between">
                  <h4 className="font-medium text-gray-900">{rec.title}</h4>
                  <PriorityBadge priority={rec.priority} />
                </div>
                <p className="text-sm text-gray-600 mt-1">{rec.reason}</p>
                
                <div className="flex flex-wrap gap-4 mt-3 text-sm">
                  {rec.expected_savings_eur && (
                    <span className="text-green-600 font-medium">
                      Tasarruf: €{rec.expected_savings_eur.toLocaleString()}/yıl
                    </span>
                  )}
                  {rec.investment_eur && (
                    <span className="text-gray-500">
                      Yatırım: €{rec.investment_eur}
                    </span>
                  )}
                  {rec.payback_years && (
                    <span className="text-gray-500">
                      Geri ödeme: {rec.payback_years} yıl
                    </span>
                  )}
                </div>
                
                {rec.first_action && (
                  <div className="mt-3 flex items-center gap-2 text-sm text-primary-600">
                    <ArrowRight className="w-4 h-4" />
                    <span>İlk adım: {rec.first_action}</span>
                  </div>
                )}
              </div>
            ))}
          </div>
        </Card>
      )}
      
      {/* Önerilmeyen Aksiyonlar */}
      {not_recommended && not_recommended.length > 0 && (
        <Card title="Şu An Önerilmeyen">
          <div className="space-y-2">
            {not_recommended.map((item, i) => (
              <div key={i} className="flex items-start gap-2 text-sm text-gray-600">
                <XCircle className="w-4 h-4 text-gray-400 shrink-0 mt-0.5" />
                <div>
                  <span className="font-medium">{item.title}:</span> {item.reason}
                </div>
              </div>
            ))}
          </div>
        </Card>
      )}
      
      {/* Aksiyon Planı */}
      {action_plan && (action_plan.immediate?.length > 0 || action_plan.short_term?.length > 0) && (
        <Card title="Zaman Çizelgesi">
          <div className="space-y-4">
            {action_plan.immediate?.length > 0 && (
              <div>
                <h4 className="text-sm font-medium text-gray-700 mb-2">Hemen (0-1 ay)</h4>
                <ul className="space-y-1">
                  {action_plan.immediate.map((item, i) => (
                    <li key={i} className="text-sm text-gray-600 flex items-center gap-2">
                      <span className="w-1.5 h-1.5 bg-red-500 rounded-full"></span>
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
            )}
            
            {action_plan.short_term?.length > 0 && (
              <div>
                <h4 className="text-sm font-medium text-gray-700 mb-2">Kısa Vade (1-6 ay)</h4>
                <ul className="space-y-1">
                  {action_plan.short_term.map((item, i) => (
                    <li key={i} className="text-sm text-gray-600 flex items-center gap-2">
                      <span className="w-1.5 h-1.5 bg-amber-500 rounded-full"></span>
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
            )}
            
            {action_plan.medium_term?.length > 0 && (
              <div>
                <h4 className="text-sm font-medium text-gray-700 mb-2">Orta Vade (6-12 ay)</h4>
                <ul className="space-y-1">
                  {action_plan.medium_term.map((item, i) => (
                    <li key={i} className="text-sm text-gray-600 flex items-center gap-2">
                      <span className="w-1.5 h-1.5 bg-blue-500 rounded-full"></span>
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </Card>
      )}
      
      {/* Uyarılar */}
      {warnings && warnings.length > 0 && (
        <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
          <div className="flex items-start gap-2">
            <AlertTriangle className="w-5 h-5 text-amber-600 shrink-0" />
            <div>
              <h4 className="font-medium text-amber-800">Dikkat</h4>
              <ul className="text-sm text-amber-700 mt-1 space-y-1">
                {warnings.map((warning, i) => (
                  <li key={i}>{warning}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      )}
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
    high: 'Yüksek',
    medium: 'Orta',
    low: 'Düşük',
  };
  
  return (
    <span className={`px-2 py-0.5 rounded text-xs font-medium ${styles[priority] || styles.low}`}>
      {labels[priority] || priority}
    </span>
  );
};

export default AIInterpretation;
```

### `/frontend/src/App.jsx` - Güncelle:

Mevcut importlara ekle:
```javascript
import AIInterpretation from './components/results/AIInterpretation';
```

useAnalysis hook'undan interpretation ve aiLoading al:
```javascript
const { result, solutions, interpretation, loading, aiLoading, error, analyze, reset } = useAnalysis();
```

Sonuç bölümünü güncelle:
```jsx
{/* Sonuçlar */}
{result && (
  <>
    <div className="border-t border-gray-200 pt-8">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Analiz Sonuçları</h2>
      <ResultsPanel data={result} />
    </div>
    
    {/* AI Yorumu */}
    <AIInterpretation 
      interpretation={interpretation} 
      loading={aiLoading} 
    />
    
    {/* AI yoksa statik öneriler göster */}
    {!interpretation && !aiLoading && solutions.length > 0 && (
      <SolutionsList solutions={solutions} />
    )}
  </>
)}
```
Brief'e eklenebilecek birkaç şey:
1. Knowledge referansı göstersin:
json{
  "recommendation": "VSD retrofit",
  "source": "/knowledge/solutions/compressor_vsd.md",
  "relevant_quote": "Yük profili %50-80 aralığında dalgalanıyorsa..."
}
```

**2. Hesaplama doğrulaması:**
Claude Code engine sonuçlarını da mantık kontrolünden geçirsin:
- "Exergy verimi %150 çıkmış — bu imkansız, hata var"
- "Yıllık kayıp negatif — parametre hatası olabilir"

**3. Sektörel bağlam:**
Kullanıcı sektör belirtirse (gıda, tekstil, otomotiv), benchmark karşılaştırması o sektö
---

## ✅ Tamamlama Kontrol Listesi

- [ ] `/skills/SKILL_exergy_interpreter.md` oluşturuldu
- [ ] `/api/services/claude_code_service.py` oluşturuldu
- [ ] `/api/routes/interpret.py` oluşturuldu
- [ ] `/api/main.py` güncellendi (interpret router)
- [ ] Frontend `api.js` güncellendi
- [ ] Frontend `useAnalysis.js` güncellendi
- [ ] `AIInterpretation.jsx` oluşturuldu
- [ ] `App.jsx` güncellendi
- [ ] Build başarılı
- [ ] Test edildi

---

## 🧪 Test

```bash
# Backend başlat
cd exergy-lab
uvicorn api.main:app --reload --port 8000

# Frontend başlat
cd frontend
npm run dev

# Manuel test: Kompresör analizi yap, AI yorumunu gözlemle
```

---

## 📝 Notlar

1. **Claude Code CLI:** Backend, `claude` CLI komutunu subprocess olarak çağırır. Claude Code'un PATH'te olması gerekir.

2. **Timeout:** AI yorumlama 60 saniye timeout'a sahip. Knowledge base büyükse artırılabilir.

3. **Graceful Degradation:** AI başarısız olursa statik öneriler gösterilir.

4. **Proje Dizini:** Claude Code `-p` flag'i ile proje dizininde çalışır, böylece /knowledge ve /skills dosyalarına erişir.

---

**Bu brief Claude Code tabanlı AI entegrasyonu için tek kaynak noktasıdır.**
