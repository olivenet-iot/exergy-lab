# ExergyLab Backend Brief

> **Claude Code için:** Bu dosyayı oku, ExergyLab projesinde backend geliştir.

---

## 🎯 Görev Özeti

ExergyLab projesi için FastAPI backend oluştur. Mevcut Python engine'i genişlet ve API endpoint'leri ile dışarıya aç.

**Mevcut durum:**
- `/engine/compressor.py` — Sadece vidalı kompresör hesabı var
- Knowledge base hazır (18 dosya)

**Hedef:**
- Tüm kompresör tipleri için engine desteği
- FastAPI endpoint'leri
- Sankey diyagram verisi üretimi
- Çözüm önerileri endpoint'i

---

## 📁 Proje Yapısı

```
exergy-lab/
├── engine/                    # Mevcut, genişletilecek
│   ├── __init__.py
│   ├── core.py               # Temel exergy fonksiyonları
│   ├── compressor.py         # Mevcut vidalı + yeni tipler
│   ├── utils.py              # Yardımcı fonksiyonlar
│   └── sankey.py             # YENİ: Sankey veri üretici
│
├── api/                       # YENİ: FastAPI backend
│   ├── __init__.py
│   ├── main.py               # FastAPI app, CORS
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── analysis.py       # /analyze endpoint
│   │   ├── benchmarks.py     # /benchmarks endpoint
│   │   └── solutions.py      # /solutions endpoint
│   └── schemas/
│       ├── __init__.py
│       ├── requests.py       # Pydantic input models
│       └── responses.py      # Pydantic output models
│
├── knowledge/                 # Mevcut, dokunma
└── requirements.txt           # Güncelle
```

---

## 🔧 BÖLÜM 1: Engine Genişletme

### 1.1 Kompresör Tipleri

`/engine/compressor.py` dosyasını genişlet. Her tip için:

#### Vidalı (Screw) — Mevcut
- `CompressorInput` ve `analyze_compressor()` zaten var
- Kontrol et, gerekirse refactor et

#### Pistonlu (Piston) — Ekle
```python
@dataclass
class PistonCompressorInput:
    power_kW: float              # Elektrik gücü
    flow_rate_m3_min: float      # Hacimsel debi
    outlet_pressure_bar: float   # Çıkış basıncı
    stages: int = 1              # Kademe sayısı (1 veya 2)
    cooling_type: str = "air"    # "air" veya "water"
    inlet_temp_C: float = 25.0
    outlet_temp_C: float = None  # Ölçülmediyse None
    operating_hours: int = 4000
    electricity_price: float = 0.10

def analyze_piston_compressor(input: PistonCompressorInput) -> CompressorResult:
    """
    Pistonlu kompresör exergy analizi.
    
    Notlar:
    - Çok kademeli için intercooling etkisi
    - Politropik katsayı n ≈ 1.3 (hava soğutmalı), n ≈ 1.1 (su soğutmalı)
    """
    pass
```

#### Scroll — Ekle
```python
@dataclass
class ScrollCompressorInput:
    power_kW: float
    flow_rate_m3_min: float
    outlet_pressure_bar: float
    oil_free: bool = False       # Yağsız mı?
    inlet_temp_C: float = 25.0
    outlet_temp_C: float = None
    operating_hours: int = 4000
    electricity_price: float = 0.10

def analyze_scroll_compressor(input: ScrollCompressorInput) -> CompressorResult:
    """Scroll kompresör exergy analizi."""
    pass
```

#### Santrifüj (Centrifugal) — Ekle
```python
@dataclass
class CentrifugalCompressorInput:
    power_kW: float
    flow_rate_m3_min: float
    outlet_pressure_bar: float
    stages: int = 1              # Kademe sayısı
    igv_position: float = 100    # Inlet Guide Vane pozisyonu (%)
    inlet_temp_C: float = 25.0
    outlet_temp_C: float = None
    operating_hours: int = 6000  # Genelde daha uzun
    electricity_price: float = 0.10

def analyze_centrifugal_compressor(input: CentrifugalCompressorInput) -> CompressorResult:
    """Santrifüj kompresör exergy analizi."""
    pass
```

### 1.2 Ortak Result Yapısı

Tüm kompresör tipleri aynı result yapısını dönsün:

```python
@dataclass
class CompressorResult:
    # Temel metrikler
    exergy_input_kW: float
    exergy_output_kW: float
    exergy_destroyed_kW: float
    exergy_efficiency_percent: float
    
    # Yıllık değerler
    annual_loss_kWh: float
    annual_cost_eur: float
    
    # Isı geri kazanım potansiyeli
    heat_recovery_potential_kW: float
    heat_recovery_exergy_kW: float
    
    # Benchmark karşılaştırma
    benchmark_rating: str  # "poor", "average", "good", "excellent"
    benchmark_percentile: float  # 0-100
    
    # Sankey için
    sankey_data: dict  # Ayrı fonksiyon üretecek
    
    # Metadata
    compressor_type: str
    calculation_timestamp: str
```

### 1.3 Sankey Veri Üretici

`/engine/sankey.py` oluştur:

```python
def generate_sankey_data(result: CompressorResult) -> dict:
    """
    Plotly Sankey diyagramı için veri üret.
    
    Akış:
    Elektrik → Kompresör → Basınçlı Hava (faydalı exergy)
                        → Yağ Soğutucu (ısı)
                        → Aftercooler (ısı)
                        → Kayıplar (entropi üretimi)
    
    Returns:
        {
            "nodes": [
                {"id": 0, "label": "Elektrik Girişi", "color": "#2196F3"},
                {"id": 1, "label": "Kompresör", "color": "#FF9800"},
                {"id": 2, "label": "Basınçlı Hava", "color": "#4CAF50"},
                {"id": 3, "label": "Isı (Geri Kazanılabilir)", "color": "#FFC107"},
                {"id": 4, "label": "Exergy Yıkımı", "color": "#F44336"},
            ],
            "links": [
                {"source": 0, "target": 1, "value": 32.0, "color": "rgba(33,150,243,0.4)"},
                {"source": 1, "target": 2, "value": 21.0, "color": "rgba(76,175,80,0.4)"},
                {"source": 1, "target": 3, "value": 8.0, "color": "rgba(255,193,7,0.4)"},
                {"source": 1, "target": 4, "value": 3.0, "color": "rgba(244,67,54,0.4)"},
            ]
        }
    """
    pass
```

---

## 🌐 BÖLÜM 2: FastAPI Backend

### 2.1 Ana Uygulama

`/api/main.py`:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ExergyLab API",
    description="Endüstriyel ekipman exergy analizi",
    version="1.0.0"
)

# CORS - React frontend için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
from api.routes import analysis, benchmarks, solutions
app.include_router(analysis.router, prefix="/api", tags=["Analysis"])
app.include_router(benchmarks.router, prefix="/api", tags=["Benchmarks"])
app.include_router(solutions.router, prefix="/api", tags=["Solutions"])

@app.get("/")
def root():
    return {"status": "ok", "service": "ExergyLab API"}

@app.get("/health")
def health():
    return {"status": "healthy"}
```

### 2.2 API Endpoints

#### POST /api/analyze

Ana analiz endpoint'i.

**Request:**
```json
{
  "compressor_type": "screw",
  "parameters": {
    "power_kW": 32,
    "flow_rate_m3_min": 6.2,
    "outlet_pressure_bar": 7.5,
    "inlet_temp_C": 25,
    "outlet_temp_C": 85,
    "operating_hours": 6000,
    "electricity_price": 0.10
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "metrics": {
      "exergy_input_kW": 32.0,
      "exergy_output_kW": 21.0,
      "exergy_destroyed_kW": 11.0,
      "exergy_efficiency_percent": 65.6,
      "annual_loss_kWh": 66000,
      "annual_cost_eur": 6600
    },
    "heat_recovery": {
      "potential_kW": 10.5,
      "recoverable_exergy_kW": 1.8,
      "annual_savings_eur": 1080
    },
    "benchmark": {
      "rating": "good",
      "percentile": 72,
      "comparison_text": "Sektör ortalamasının üzerinde"
    },
    "sankey": {
      "nodes": [...],
      "links": [...]
    }
  },
  "metadata": {
    "compressor_type": "screw",
    "calculation_timestamp": "2026-01-31T19:30:00Z",
    "engine_version": "1.0.0"
  }
}
```

#### GET /api/benchmarks/{compressor_type}

Benchmark verileri.

**Response:**
```json
{
  "compressor_type": "screw",
  "exergy_efficiency": {
    "poor": {"max": 30},
    "average": {"min": 30, "max": 45},
    "good": {"min": 45, "max": 55},
    "excellent": {"min": 60}
  },
  "specific_power": {
    "excellent": {"max": 5.5},
    "good": {"min": 5.5, "max": 6.5},
    "average": {"min": 6.5, "max": 7.5},
    "poor": {"min": 7.5}
  },
  "sector_averages": {
    "automotive": 42,
    "food_beverage": 38,
    "textile": 35,
    "general_manufacturing": 40
  }
}
```

#### GET /api/solutions/{compressor_type}

Çözüm önerileri.

**Query params:**
- `efficiency`: Mevcut exergy verimi (%)
- `specific_power`: Spesifik güç (kW per m³/min)
- `operating_hours`: Yıllık çalışma saati

**Response:**
```json
{
  "recommendations": [
    {
      "id": "vsd_retrofit",
      "title": "VSD (Değişken Hız Sürücü) Retrofit",
      "priority": "high",
      "potential_savings_percent": "20-35",
      "estimated_investment_eur": "8000-15000",
      "estimated_roi_years": 1.5,
      "description": "Değişken yük profilinde önemli tasarruf sağlar",
      "applicable_when": "Yük profili %50-80 aralığında dalgalanıyorsa",
      "knowledge_base_ref": "/knowledge/solutions/compressor_vsd.md"
    },
    {
      "id": "leak_detection",
      "title": "Kaçak Tespiti ve Giderme",
      "priority": "high",
      "potential_savings_percent": "10-30",
      "estimated_investment_eur": "500-2000",
      "estimated_roi_years": 0.5,
      "description": "Tipik tesislerde %20-30 kaçak oranı var",
      "applicable_when": "Kaçak taraması yapılmamışsa",
      "knowledge_base_ref": "/knowledge/solutions/compressor_air_leaks.md"
    },
    {
      "id": "pressure_optimization",
      "title": "Basınç Optimizasyonu",
      "priority": "medium",
      "potential_savings_percent": "6-7 per bar",
      "estimated_investment_eur": "0-500",
      "estimated_roi_years": 0.1,
      "description": "Her 1 bar düşüş ≈ %6-7 enerji tasarrufu",
      "applicable_when": "Sistem basıncı gerçek ihtiyacın üzerindeyse",
      "knowledge_base_ref": "/knowledge/solutions/compressor_pressure_optimization.md"
    }
  ]
}
```

#### GET /api/compressor-types

Desteklenen kompresör tipleri ve form alanları.

**Response:**
```json
{
  "types": [
    {
      "id": "screw",
      "name": "Vidalı Kompresör",
      "name_en": "Screw Compressor",
      "icon": "settings",
      "fields": [
        {
          "id": "power_kW",
          "label": "Elektrik Gücü",
          "unit": "kW",
          "type": "number",
          "required": true,
          "min": 1,
          "max": 500,
          "default": 37,
          "help": "Ölçülen veya nameplate değeri"
        },
        {
          "id": "flow_rate_m3_min",
          "label": "Hava Debisi",
          "unit": "m³/min",
          "type": "number",
          "required": true,
          "min": 0.1,
          "max": 100,
          "help": "Nameplate veya flowmeter ölçümü"
        },
        {
          "id": "outlet_pressure_bar",
          "label": "Çıkış Basıncı",
          "unit": "bar",
          "type": "number",
          "required": true,
          "min": 4,
          "max": 15,
          "default": 7.5
        },
        {
          "id": "inlet_temp_C",
          "label": "Giriş Sıcaklığı",
          "unit": "°C",
          "type": "number",
          "required": false,
          "default": 25,
          "help": "Ortam sıcaklığı"
        },
        {
          "id": "outlet_temp_C",
          "label": "Çıkış Sıcaklığı",
          "unit": "°C",
          "type": "number",
          "required": false,
          "default": 85,
          "help": "Ölçülmediyse boş bırakın"
        },
        {
          "id": "operating_hours",
          "label": "Yıllık Çalışma Saati",
          "unit": "saat/yıl",
          "type": "number",
          "required": false,
          "default": 4000,
          "min": 100,
          "max": 8760
        },
        {
          "id": "electricity_price",
          "label": "Elektrik Fiyatı",
          "unit": "€/kWh",
          "type": "number",
          "required": false,
          "default": 0.10,
          "step": 0.01
        }
      ]
    },
    {
      "id": "piston",
      "name": "Pistonlu Kompresör",
      "name_en": "Reciprocating Compressor",
      "icon": "piston",
      "fields": [
        // ... benzer yapı, ek alanlar: stages, cooling_type
      ]
    },
    {
      "id": "scroll",
      "name": "Scroll Kompresör",
      "icon": "spiral",
      "fields": [
        // ... benzer yapı, ek alan: oil_free
      ]
    },
    {
      "id": "centrifugal",
      "name": "Santrifüj Kompresör",
      "icon": "rotate",
      "fields": [
        // ... benzer yapı, ek alanlar: stages, igv_position
      ]
    }
  ]
}
```

### 2.3 Pydantic Schemas

`/api/schemas/requests.py`:

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal

class AnalysisRequest(BaseModel):
    compressor_type: Literal["screw", "piston", "scroll", "centrifugal"]
    parameters: dict  # Dinamik, tipe göre değişir
    
class ScrewCompressorParams(BaseModel):
    power_kW: float = Field(..., gt=0, le=500)
    flow_rate_m3_min: float = Field(..., gt=0, le=100)
    outlet_pressure_bar: float = Field(..., ge=4, le=15)
    inlet_temp_C: Optional[float] = 25.0
    outlet_temp_C: Optional[float] = None
    operating_hours: Optional[int] = 4000
    electricity_price: Optional[float] = 0.10

# Diğer tipler için benzer...
```

`/api/schemas/responses.py`:

```python
from pydantic import BaseModel
from typing import List, Optional

class MetricsResponse(BaseModel):
    exergy_input_kW: float
    exergy_output_kW: float
    exergy_destroyed_kW: float
    exergy_efficiency_percent: float
    annual_loss_kWh: float
    annual_cost_eur: float

class HeatRecoveryResponse(BaseModel):
    potential_kW: float
    recoverable_exergy_kW: float
    annual_savings_eur: float

class BenchmarkResponse(BaseModel):
    rating: str
    percentile: float
    comparison_text: str

class SankeyNode(BaseModel):
    id: int
    label: str
    color: str

class SankeyLink(BaseModel):
    source: int
    target: int
    value: float
    color: str

class SankeyResponse(BaseModel):
    nodes: List[SankeyNode]
    links: List[SankeyLink]

class AnalysisResponse(BaseModel):
    success: bool
    data: dict
    metadata: dict
```

---

## 🧪 BÖLÜM 3: Test

### 3.1 Engine Testleri

`/tests/test_compressor_types.py`:

```python
def test_screw_compressor():
    """Mevcut vidalı kompresör testi"""
    input_data = ScrewCompressorInput(
        power_kW=32,
        flow_rate_m3_min=6.2,
        outlet_pressure_bar=7.5
    )
    result = analyze_screw_compressor(input_data)
    
    assert 60 < result.exergy_efficiency_percent < 70
    assert result.exergy_destroyed_kW > 0
    assert result.benchmark_rating in ["poor", "average", "good", "excellent"]

def test_piston_compressor():
    """Pistonlu kompresör testi"""
    pass

def test_scroll_compressor():
    """Scroll kompresör testi"""
    pass

def test_centrifugal_compressor():
    """Santrifüj kompresör testi"""
    pass

def test_sankey_data_generation():
    """Sankey veri üretimi testi"""
    pass
```

### 3.2 API Testleri

`/tests/test_api.py`:

```python
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_analyze_screw():
    response = client.post("/api/analyze", json={
        "compressor_type": "screw",
        "parameters": {
            "power_kW": 32,
            "flow_rate_m3_min": 6.2,
            "outlet_pressure_bar": 7.5
        }
    })
    assert response.status_code == 200
    assert response.json()["success"] == True
    assert "sankey" in response.json()["data"]

def test_get_compressor_types():
    response = client.get("/api/compressor-types")
    assert response.status_code == 200
    assert len(response.json()["types"]) >= 4
```

---

## 📦 BÖLÜM 4: Dependencies

`requirements.txt` güncelle:

```
# Mevcut
CoolProp>=6.4.0
numpy>=1.21.0
pandas>=1.3.0
pydantic>=2.0.0

# Yeni - API
fastapi>=0.109.0
uvicorn>=0.27.0
python-multipart>=0.0.6

# Test
pytest>=7.0.0
httpx>=0.26.0  # FastAPI test client için
```

---

## 🚀 Çalıştırma

```bash
# API'yi başlat
cd exergy-lab
uvicorn api.main:app --reload --port 8000

# Test
pytest tests/ -v
```

API Swagger UI: http://localhost:8000/docs

---

## ✅ Tamamlama Kontrol Listesi

Backend tamamlandığında:

- [ ] Engine: 4 kompresör tipi çalışıyor (screw, piston, scroll, centrifugal)
- [ ] Engine: Sankey veri üretici çalışıyor
- [ ] API: `/api/analyze` endpoint çalışıyor
- [ ] API: `/api/benchmarks/{type}` endpoint çalışıyor
- [ ] API: `/api/solutions/{type}` endpoint çalışıyor
- [ ] API: `/api/compressor-types` endpoint çalışıyor
- [ ] API: CORS ayarlı (localhost:5173, localhost:3000)
- [ ] Testler geçiyor
- [ ] Swagger UI çalışıyor

**Test komutu:**
```bash
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"compressor_type":"screw","parameters":{"power_kW":32,"flow_rate_m3_min":6.2,"outlet_pressure_bar":7.5}}'
```

---

**Bu brief backend geliştirme için tek kaynak noktasıdır.**
