# ExergyLab Büyük Refactoring Brief

> **Claude Code için:** Bu dosyayı oku ve ExergyLab'ı multi-equipment destekleyecek şekilde refactor et.

---

## 🎯 Görev Özeti

ExergyLab şu an sadece kompresör için çalışıyor. Artık 4 ekipman tipi var (kompresör, kazan, chiller, pompa) ve fabrika seviyesi analiz yapılacak.

**Yapılacaklar:**
1. Knowledge base klasör yapısını reorganize et
2. Backend'i generic multi-equipment destekleyecek şekilde güncelle
3. Frontend'e sidebar navigation ve routing ekle
4. Fabrika analizi için temel altyapı oluştur

---

## 📁 BÖLÜM 1: Knowledge Base Reorganizasyonu

### 1.1 Mevcut Yapı (Değiştirilecek)

```
knowledge/
├── equipment/
│   ├── boiler_*.md, chiller_*.md, compressor_*.md, pump_*.md (HEPSİ KARIŞIK)
├── solutions/
│   ├── boiler_*.md, chiller_*.md, compressor_*.md, pump_*.md (HEPSİ KARIŞIK)
├── benchmarks/
│   ├── boiler_benchmarks.md, chiller_benchmarks.md, compressor_benchmarks.md, pump_benchmarks.md
├── formulas/
│   └── ... (aynı şekilde)
└── methodology/
    └── ... (aynı şekilde)
```

### 1.2 Hedef Yapı

```
knowledge/
├── compressor/
│   ├── equipment/
│   │   ├── screw.md
│   │   ├── screw_oilfree.md
│   │   ├── piston.md
│   │   ├── scroll.md
│   │   ├── centrifugal.md
│   │   ├── roots.md
│   │   └── systems_overview.md
│   ├── solutions/
│   │   ├── vsd.md
│   │   ├── air_leaks.md
│   │   ├── pressure_optimization.md
│   │   ├── heat_recovery.md
│   │   ├── maintenance.md
│   │   ├── dryer_optimization.md
│   │   ├── inlet_optimization.md
│   │   └── system_design.md
│   ├── benchmarks.md
│   ├── formulas.md
│   └── audit.md
│
├── boiler/
│   ├── equipment/
│   │   ├── steam_firetube.md
│   │   ├── steam_watertube.md
│   │   ├── hotwater.md
│   │   ├── condensing.md
│   │   ├── waste_heat.md
│   │   ├── electric.md
│   │   ├── biomass.md
│   │   ├── fuels.md
│   │   └── systems_overview.md
│   ├── solutions/
│   │   ├── economizer.md
│   │   ├── air_preheater.md
│   │   ├── oxygen_control.md
│   │   ├── blowdown_recovery.md
│   │   ├── condensate_return.md
│   │   ├── steam_trap.md
│   │   ├── insulation.md
│   │   ├── load_optimization.md
│   │   ├── combustion_tuning.md
│   │   └── feedwater_treatment.md
│   ├── benchmarks.md
│   ├── formulas.md
│   └── audit.md
│
├── chiller/
│   ├── equipment/
│   │   ├── vapor_compression.md
│   │   ├── screw.md
│   │   ├── centrifugal.md
│   │   ├── scroll.md
│   │   ├── reciprocating.md
│   │   ├── absorption.md
│   │   ├── air_cooled.md
│   │   ├── water_cooled.md
│   │   ├── refrigerants.md
│   │   ├── cooling_tower.md
│   │   └── systems_overview.md
│   ├── solutions/
│   │   ├── vsd.md
│   │   ├── condenser_optimization.md
│   │   ├── chilled_water_reset.md
│   │   ├── free_cooling.md
│   │   ├── sequencing.md
│   │   ├── maintenance.md
│   │   ├── load_reduction.md
│   │   ├── delta_t.md
│   │   ├── thermal_storage.md
│   │   └── heat_recovery.md
│   ├── benchmarks.md
│   ├── formulas.md
│   └── audit.md
│
├── pump/
│   ├── equipment/
│   │   ├── centrifugal.md
│   │   ├── positive_displacement.md
│   │   ├── submersible.md
│   │   ├── vertical_turbine.md
│   │   ├── axial_mixed.md
│   │   ├── vacuum.md
│   │   ├── booster.md
│   │   ├── motors_drives.md
│   │   └── systems_overview.md
│   ├── solutions/
│   │   ├── vsd.md
│   │   ├── impeller_trimming.md
│   │   ├── right_sizing.md
│   │   ├── parallel_operation.md
│   │   ├── system_optimization.md
│   │   ├── motor_upgrade.md
│   │   ├── maintenance.md
│   │   ├── throttle_elimination.md
│   │   ├── cavitation_prevention.md
│   │   └── control_optimization.md
│   ├── benchmarks.md
│   ├── formulas.md
│   └── audit.md
│
└── factory/
    ├── methodology.md          # Fabrika seviyesi audit
    ├── system_integration.md   # Ekipmanlar arası entegrasyon
    └── energy_flow.md          # Enerji/exergy akış analizi
```

### 1.3 Taşıma Scripti

Bash ile dosyaları taşı:

```bash
#!/bin/bash
cd /home/ubuntu/exergy-lab/knowledge

# Kompresör
mkdir -p compressor/equipment compressor/solutions
mv equipment/compressor_*.md compressor/equipment/
mv equipment/compressed_air_systems.md compressor/equipment/systems_overview.md
mv solutions/compressor_*.md compressor/solutions/
mv benchmarks/compressor_benchmarks.md compressor/benchmarks.md
mv formulas/compressor_exergy.md compressor/formulas.md
mv methodology/compressed_air_audit.md compressor/audit.md

# Dosya isimlerinden prefix'leri kaldır
cd compressor/equipment
for f in compressor_*.md; do mv "$f" "${f#compressor_}"; done
cd ../solutions
for f in compressor_*.md; do mv "$f" "${f#compressor_}"; done

# Kazan
cd /home/ubuntu/exergy-lab/knowledge
mkdir -p boiler/equipment boiler/solutions
mv equipment/boiler_*.md boiler/equipment/
mv equipment/steam_systems_overview.md boiler/equipment/systems_overview.md
mv solutions/boiler_*.md boiler/solutions/
mv benchmarks/boiler_benchmarks.md boiler/benchmarks.md
mv formulas/boiler_exergy.md boiler/formulas.md
mv methodology/boiler_audit.md boiler/audit.md

cd boiler/equipment
for f in boiler_*.md; do mv "$f" "${f#boiler_}"; done
cd ../solutions
for f in boiler_*.md; do mv "$f" "${f#boiler_}"; done

# Chiller
cd /home/ubuntu/exergy-lab/knowledge
mkdir -p chiller/equipment chiller/solutions
mv equipment/chiller_*.md chiller/equipment/
mv equipment/chilled_water_systems.md chiller/equipment/systems_overview.md
mv equipment/cooling_tower.md chiller/equipment/
mv solutions/chiller_*.md chiller/solutions/
mv benchmarks/chiller_benchmarks.md chiller/benchmarks.md
mv formulas/chiller_exergy.md chiller/formulas.md
mv methodology/chiller_audit.md chiller/audit.md

cd chiller/equipment
for f in chiller_*.md; do mv "$f" "${f#chiller_}"; done
cd ../solutions
for f in chiller_*.md; do mv "$f" "${f#chiller_}"; done

# Pompa
cd /home/ubuntu/exergy-lab/knowledge
mkdir -p pump/equipment pump/solutions
mv equipment/pump_*.md pump/equipment/
mv equipment/pumping_systems_overview.md pump/equipment/systems_overview.md
mv solutions/pump_*.md pump/solutions/
mv benchmarks/pump_benchmarks.md pump/benchmarks.md
mv formulas/pump_exergy.md pump/formulas.md
mv methodology/pump_audit.md pump/audit.md

cd pump/equipment
for f in pump_*.md; do mv "$f" "${f#pump_}"; done
cd ../solutions
for f in pump_*.md; do mv "$f" "${f#pump_}"; done

# Fabrika klasörü oluştur
cd /home/ubuntu/exergy-lab/knowledge
mkdir -p factory

# Boş klasörleri temizle
rmdir equipment solutions benchmarks formulas methodology 2>/dev/null || true
```

### 1.4 Doğrulama

Taşıma sonrası yapıyı kontrol et:

```bash
find knowledge -type f -name "*.md" | wc -l  # Toplam dosya sayısı
tree knowledge -L 3  # Klasör yapısı
```

---

## 🔧 BÖLÜM 2: Backend Refactoring

### 2.1 Yeni Dosya Yapısı

```
api/
├── main.py                    # Güncelle: yeni router'lar
├── routes/
│   ├── analysis.py            # Güncelle: generic equipment support
│   ├── benchmarks.py          # Güncelle: equipment_type parametresi
│   ├── solutions.py           # Güncelle: equipment_type parametresi
│   ├── interpret.py           # Güncelle: equipment_type desteği
│   └── factory.py             # YENİ: fabrika analizi
├── schemas/
│   ├── requests.py            # Güncelle: tüm ekipman tipleri
│   └── responses.py           # Güncelle: generic response
└── services/
    ├── claude_code_service.py # Güncelle: knowledge path
    └── equipment_registry.py  # YENİ: ekipman tipi registry
```

### 2.2 Equipment Registry

`/api/services/equipment_registry.py`:

```python
"""
Ekipman tipi registry - desteklenen ekipmanlar ve özellikleri
"""

EQUIPMENT_TYPES = {
    "compressor": {
        "name": "Kompresör",
        "name_en": "Compressor",
        "icon": "wind",
        "subtypes": [
            {"id": "screw", "name": "Vidalı", "name_en": "Screw"},
            {"id": "screw_oilfree", "name": "Yağsız Vidalı", "name_en": "Oil-free Screw"},
            {"id": "piston", "name": "Pistonlu", "name_en": "Reciprocating"},
            {"id": "scroll", "name": "Scroll", "name_en": "Scroll"},
            {"id": "centrifugal", "name": "Santrifüj", "name_en": "Centrifugal"},
            {"id": "roots", "name": "Roots Blower", "name_en": "Roots"},
        ],
        "knowledge_path": "knowledge/compressor",
        "engine_module": "engine.compressor",
    },
    "boiler": {
        "name": "Kazan",
        "name_en": "Boiler",
        "icon": "flame",
        "subtypes": [
            {"id": "steam_firetube", "name": "Ateş Borulu Buhar", "name_en": "Fire-tube Steam"},
            {"id": "steam_watertube", "name": "Su Borulu Buhar", "name_en": "Water-tube Steam"},
            {"id": "hotwater", "name": "Sıcak Su", "name_en": "Hot Water"},
            {"id": "condensing", "name": "Yoğuşmalı", "name_en": "Condensing"},
            {"id": "waste_heat", "name": "Atık Isı / HRSG", "name_en": "Waste Heat"},
            {"id": "electric", "name": "Elektrikli", "name_en": "Electric"},
            {"id": "biomass", "name": "Biyokütle", "name_en": "Biomass"},
        ],
        "knowledge_path": "knowledge/boiler",
        "engine_module": "engine.boiler",
    },
    "chiller": {
        "name": "Chiller",
        "name_en": "Chiller",
        "icon": "snowflake",
        "subtypes": [
            {"id": "screw", "name": "Vidalı", "name_en": "Screw"},
            {"id": "centrifugal", "name": "Santrifüj", "name_en": "Centrifugal"},
            {"id": "scroll", "name": "Scroll", "name_en": "Scroll"},
            {"id": "reciprocating", "name": "Pistonlu", "name_en": "Reciprocating"},
            {"id": "absorption", "name": "Absorpsiyonlu", "name_en": "Absorption"},
            {"id": "air_cooled", "name": "Hava Soğutmalı", "name_en": "Air-cooled"},
            {"id": "water_cooled", "name": "Su Soğutmalı", "name_en": "Water-cooled"},
        ],
        "knowledge_path": "knowledge/chiller",
        "engine_module": "engine.chiller",
    },
    "pump": {
        "name": "Pompa",
        "name_en": "Pump",
        "icon": "droplets",
        "subtypes": [
            {"id": "centrifugal", "name": "Santrifüj", "name_en": "Centrifugal"},
            {"id": "positive_displacement", "name": "Pozitif Deplasmanlı", "name_en": "Positive Displacement"},
            {"id": "submersible", "name": "Dalgıç", "name_en": "Submersible"},
            {"id": "vertical_turbine", "name": "Dikey Türbin", "name_en": "Vertical Turbine"},
            {"id": "booster", "name": "Hidrofor", "name_en": "Booster"},
            {"id": "vacuum", "name": "Vakum", "name_en": "Vacuum"},
        ],
        "knowledge_path": "knowledge/pump",
        "engine_module": "engine.pump",
    },
}


def get_equipment_types():
    """Tüm ekipman tiplerini döndür (frontend için)"""
    return [
        {
            "id": eq_id,
            "name": eq_data["name"],
            "name_en": eq_data["name_en"],
            "icon": eq_data["icon"],
            "subtypes": eq_data["subtypes"],
        }
        for eq_id, eq_data in EQUIPMENT_TYPES.items()
    ]


def get_equipment_subtypes(equipment_type: str):
    """Belirli bir ekipman tipinin alt tiplerini döndür"""
    if equipment_type not in EQUIPMENT_TYPES:
        return []
    return EQUIPMENT_TYPES[equipment_type]["subtypes"]


def get_knowledge_path(equipment_type: str) -> str:
    """Ekipman tipinin knowledge base path'ini döndür"""
    if equipment_type not in EQUIPMENT_TYPES:
        return "knowledge"
    return EQUIPMENT_TYPES[equipment_type]["knowledge_path"]


def is_valid_equipment(equipment_type: str, subtype: str = None) -> bool:
    """Ekipman tipi ve alt tipi geçerli mi?"""
    if equipment_type not in EQUIPMENT_TYPES:
        return False
    if subtype:
        valid_subtypes = [s["id"] for s in EQUIPMENT_TYPES[equipment_type]["subtypes"]]
        return subtype in valid_subtypes
    return True
```

### 2.3 API Routes Güncelleme

`/api/routes/analysis.py` güncelle:

```python
from fastapi import APIRouter, HTTPException
from api.services.equipment_registry import (
    get_equipment_types,
    get_equipment_subtypes,
    is_valid_equipment,
)

router = APIRouter()


@router.get("/equipment-types")
def list_equipment_types():
    """Tüm desteklenen ekipman tiplerini listele"""
    return {"equipment_types": get_equipment_types()}


@router.get("/equipment-types/{equipment_type}/subtypes")
def list_subtypes(equipment_type: str):
    """Belirli ekipman tipinin alt tiplerini listele"""
    if not is_valid_equipment(equipment_type):
        raise HTTPException(status_code=404, detail=f"Unknown equipment type: {equipment_type}")
    return {"subtypes": get_equipment_subtypes(equipment_type)}


@router.post("/analyze")
async def analyze_equipment(request: dict):
    """
    Generic ekipman analizi.
    
    Request:
    {
        "equipment_type": "compressor",  # veya boiler, chiller, pump
        "subtype": "screw",
        "parameters": {...}
    }
    """
    equipment_type = request.get("equipment_type")
    subtype = request.get("subtype")
    parameters = request.get("parameters", {})
    
    if not is_valid_equipment(equipment_type, subtype):
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid equipment: {equipment_type}/{subtype}"
        )
    
    # Engine modülünü dinamik olarak yükle
    try:
        if equipment_type == "compressor":
            from engine.compressor import analyze_compressor
            result = analyze_compressor(subtype, parameters)
        elif equipment_type == "boiler":
            from engine.boiler import analyze_boiler
            result = analyze_boiler(subtype, parameters)
        elif equipment_type == "chiller":
            from engine.chiller import analyze_chiller
            result = analyze_chiller(subtype, parameters)
        elif equipment_type == "pump":
            from engine.pump import analyze_pump
            result = analyze_pump(subtype, parameters)
        else:
            raise HTTPException(status_code=400, detail="Unsupported equipment type")
            
        return {
            "success": True,
            "data": result,
            "metadata": {
                "equipment_type": equipment_type,
                "subtype": subtype,
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### 2.4 Skills Dosyası Güncelleme

`/skills/SKILL_exergy_interpreter.md` dosyasını güncelle:
- Knowledge path'leri yeni yapıya göre güncelle
- Tüm ekipman tipleri için yorumlama kuralları ekle

---

## 🎨 BÖLÜM 3: Frontend Refactoring

### 3.1 Yeni Dosya Yapısı

```
frontend/src/
├── components/
│   ├── layout/
│   │   ├── Sidebar.jsx          # YENİ: Sol menü
│   │   ├── Header.jsx           # Güncelle
│   │   └── Layout.jsx           # Güncelle: sidebar entegrasyonu
│   ├── equipment/
│   │   ├── EquipmentSelector.jsx    # YENİ: Ekipman tipi seçici
│   │   ├── SubtypeSelector.jsx      # YENİ: Alt tip seçici
│   │   ├── ParameterForm.jsx        # Güncelle: dinamik alanlar
│   │   └── AnalysisPage.jsx         # YENİ: Generic analiz sayfası
│   ├── factory/
│   │   ├── FactoryDashboard.jsx     # YENİ
│   │   ├── EquipmentInventory.jsx   # YENİ
│   │   └── FactorySankey.jsx        # YENİ
│   ├── results/
│   │   └── ... (mevcut, güncelle)
│   └── common/
│       └── ... (mevcut)
├── pages/
│   ├── Dashboard.jsx            # YENİ: Ana sayfa
│   ├── EquipmentAnalysis.jsx    # YENİ: /equipment/:type
│   ├── FactoryAnalysis.jsx      # YENİ: /factory/:id
│   └── Reports.jsx              # YENİ: /reports
├── hooks/
│   ├── useEquipmentTypes.js     # YENİ: Ekipman tipleri
│   └── useAnalysis.js           # Güncelle
├── services/
│   └── api.js                   # Güncelle: yeni endpoint'ler
└── App.jsx                      # Güncelle: routing
```

### 3.2 React Router Kurulumu

```bash
cd frontend
npm install react-router-dom
```

### 3.3 App.jsx (Routing)

```jsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/layout/Layout';
import Dashboard from './pages/Dashboard';
import EquipmentAnalysis from './pages/EquipmentAnalysis';
import FactoryAnalysis from './pages/FactoryAnalysis';
import Reports from './pages/Reports';

function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/equipment/:equipmentType" element={<EquipmentAnalysis />} />
          <Route path="/factory" element={<FactoryAnalysis />} />
          <Route path="/factory/:projectId" element={<FactoryAnalysis />} />
          <Route path="/reports" element={<Reports />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

export default App;
```

### 3.4 Sidebar Component

`/frontend/src/components/layout/Sidebar.jsx`:

```jsx
import { NavLink } from 'react-router-dom';
import { 
  LayoutDashboard, 
  Wind, 
  Flame, 
  Snowflake, 
  Droplets,
  Factory,
  FolderOpen,
  ChevronDown,
  ChevronRight
} from 'lucide-react';
import { useState } from 'react';

const EQUIPMENT_ITEMS = [
  { id: 'compressor', name: 'Kompresör', icon: Wind },
  { id: 'boiler', name: 'Kazan', icon: Flame },
  { id: 'chiller', name: 'Chiller', icon: Snowflake },
  { id: 'pump', name: 'Pompa', icon: Droplets },
];

const Sidebar = () => {
  const [equipmentOpen, setEquipmentOpen] = useState(true);
  const [factoryOpen, setFactoryOpen] = useState(true);

  const navLinkClass = ({ isActive }) =>
    `flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors ${
      isActive
        ? 'bg-primary-100 text-primary-700 font-medium'
        : 'text-gray-600 hover:bg-gray-100'
    }`;

  return (
    <aside className="w-64 bg-white border-r border-gray-200 h-screen sticky top-0">
      <div className="p-4">
        {/* Logo */}
        <div className="flex items-center gap-3 mb-8">
          <div className="w-10 h-10 bg-primary-600 rounded-lg flex items-center justify-center">
            <span className="text-white font-bold text-lg">Ex</span>
          </div>
          <div>
            <h1 className="font-bold text-gray-900">ExergyLab</h1>
            <p className="text-xs text-gray-500">Termodinamik Analiz</p>
          </div>
        </div>

        {/* Navigation */}
        <nav className="space-y-1">
          {/* Dashboard */}
          <NavLink to="/" className={navLinkClass} end>
            <LayoutDashboard className="w-5 h-5" />
            Dashboard
          </NavLink>

          {/* Ekipman Analizi */}
          <div className="pt-4">
            <button
              onClick={() => setEquipmentOpen(!equipmentOpen)}
              className="flex items-center justify-between w-full px-3 py-2 text-sm font-medium text-gray-900"
            >
              <span className="flex items-center gap-2">
                🔧 Ekipman Analizi
              </span>
              {equipmentOpen ? (
                <ChevronDown className="w-4 h-4" />
              ) : (
                <ChevronRight className="w-4 h-4" />
              )}
            </button>
            
            {equipmentOpen && (
              <div className="ml-4 space-y-1 mt-1">
                {EQUIPMENT_ITEMS.map((item) => (
                  <NavLink
                    key={item.id}
                    to={`/equipment/${item.id}`}
                    className={navLinkClass}
                  >
                    <item.icon className="w-4 h-4" />
                    {item.name}
                  </NavLink>
                ))}
              </div>
            )}
          </div>

          {/* Fabrika Analizi */}
          <div className="pt-4">
            <button
              onClick={() => setFactoryOpen(!factoryOpen)}
              className="flex items-center justify-between w-full px-3 py-2 text-sm font-medium text-gray-900"
            >
              <span className="flex items-center gap-2">
                🏭 Fabrika Analizi
              </span>
              {factoryOpen ? (
                <ChevronDown className="w-4 h-4" />
              ) : (
                <ChevronRight className="w-4 h-4" />
              )}
            </button>
            
            {factoryOpen && (
              <div className="ml-4 space-y-1 mt-1">
                <NavLink to="/factory" className={navLinkClass}>
                  <Factory className="w-4 h-4" />
                  Yeni Proje
                </NavLink>
                <NavLink to="/reports" className={navLinkClass}>
                  <FolderOpen className="w-4 h-4" />
                  Raporlar
                </NavLink>
              </div>
            )}
          </div>
        </nav>
      </div>
    </aside>
  );
};

export default Sidebar;
```

### 3.5 Layout Component Güncelleme

`/frontend/src/components/layout/Layout.jsx`:

```jsx
import Sidebar from './Sidebar';
import Header from './Header';

const Layout = ({ children }) => {
  return (
    <div className="flex min-h-screen bg-gray-50">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Header />
        <main className="flex-1 p-6 overflow-auto">
          {children}
        </main>
      </div>
    </div>
  );
};

export default Layout;
```

### 3.6 Equipment Analysis Page

`/frontend/src/pages/EquipmentAnalysis.jsx`:

```jsx
import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import SubtypeSelector from '../components/equipment/SubtypeSelector';
import ParameterForm from '../components/forms/ParameterForm';
import ResultsPanel from '../components/results/ResultsPanel';
import AIInterpretation from '../components/results/AIInterpretation';
import Card from '../components/common/Card';
import { useAnalysis } from '../hooks/useAnalysis';
import { getEquipmentSubtypes } from '../services/api';

const EQUIPMENT_NAMES = {
  compressor: 'Kompresör',
  boiler: 'Kazan',
  chiller: 'Chiller',
  pump: 'Pompa',
};

const EquipmentAnalysis = () => {
  const { equipmentType } = useParams();
  const [subtypes, setSubtypes] = useState([]);
  const [selectedSubtype, setSelectedSubtype] = useState(null);
  const [formValues, setFormValues] = useState({});
  const [loading, setLoading] = useState(true);
  
  const { result, interpretation, loading: analyzing, aiLoading, error, analyze, reset } = useAnalysis();

  // Alt tipleri yükle
  useEffect(() => {
    const loadSubtypes = async () => {
      setLoading(true);
      try {
        const data = await getEquipmentSubtypes(equipmentType);
        setSubtypes(data.subtypes || []);
        setSelectedSubtype(null);
        setFormValues({});
        reset();
      } catch (err) {
        console.error('Failed to load subtypes:', err);
      }
      setLoading(false);
    };
    
    loadSubtypes();
  }, [equipmentType]);

  const handleSubtypeSelect = (subtypeId) => {
    setSelectedSubtype(subtypeId);
    setFormValues({});
    reset();
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    analyze(equipmentType, selectedSubtype, formValues);
  };

  const equipmentName = EQUIPMENT_NAMES[equipmentType] || equipmentType;

  return (
    <div className="space-y-6 max-w-6xl mx-auto">
      {/* Başlık */}
      <div>
        <h1 className="text-2xl font-bold text-gray-900">
          {equipmentName} Exergy Analizi
        </h1>
        <p className="text-gray-600 mt-1">
          {equipmentName} tipini seçin ve parametreleri girin
        </p>
      </div>

      {/* Alt Tip Seçimi */}
      <Card title={`1. ${equipmentName} Tipi`}>
        {loading ? (
          <div className="h-24 flex items-center justify-center">
            <span className="text-gray-400">Yükleniyor...</span>
          </div>
        ) : (
          <SubtypeSelector
            subtypes={subtypes}
            selected={selectedSubtype}
            onSelect={handleSubtypeSelect}
          />
        )}
      </Card>

      {/* Parametre Formu */}
      {selectedSubtype && (
        <Card title="2. Parametreler">
          <ParameterForm
            equipmentType={equipmentType}
            subtype={selectedSubtype}
            values={formValues}
            onChange={(id, value) => setFormValues(prev => ({ ...prev, [id]: value }))}
            onSubmit={handleSubmit}
            loading={analyzing}
          />
        </Card>
      )}

      {/* Hata */}
      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700">
          {error}
        </div>
      )}

      {/* Sonuçlar */}
      {result && (
        <>
          <div className="border-t border-gray-200 pt-6">
            <h2 className="text-xl font-bold text-gray-900 mb-4">Analiz Sonuçları</h2>
            <ResultsPanel data={result} />
          </div>

          <AIInterpretation interpretation={interpretation} loading={aiLoading} />
        </>
      )}
    </div>
  );
};

export default EquipmentAnalysis;
```

### 3.7 Dashboard Page

`/frontend/src/pages/Dashboard.jsx`:

```jsx
import { Link } from 'react-router-dom';
import { Wind, Flame, Snowflake, Droplets, ArrowRight } from 'lucide-react';
import Card from '../components/common/Card';

const EQUIPMENT_CARDS = [
  {
    id: 'compressor',
    name: 'Kompresör',
    description: 'Basınçlı hava sistemleri exergy analizi',
    icon: Wind,
    color: 'bg-blue-500',
    stats: '4 tip desteklenir',
  },
  {
    id: 'boiler',
    name: 'Kazan',
    description: 'Buhar ve sıcak su kazanları exergy analizi',
    icon: Flame,
    color: 'bg-orange-500',
    stats: '7 tip desteklenir',
  },
  {
    id: 'chiller',
    name: 'Chiller',
    description: 'Soğutma sistemleri exergy analizi',
    icon: Snowflake,
    color: 'bg-cyan-500',
    stats: '7 tip desteklenir',
  },
  {
    id: 'pump',
    name: 'Pompa',
    description: 'Pompalama sistemleri exergy analizi',
    icon: Droplets,
    color: 'bg-emerald-500',
    stats: '6 tip desteklenir',
  },
];

const Dashboard = () => {
  return (
    <div className="space-y-8 max-w-6xl mx-auto">
      {/* Welcome */}
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Hoş Geldiniz</h1>
        <p className="text-gray-600 mt-2">
          ExergyLab ile endüstriyel ekipmanlarınızın termodinamik performansını analiz edin
        </p>
      </div>

      {/* Equipment Cards */}
      <div>
        <h2 className="text-lg font-semibold text-gray-900 mb-4">Ekipman Analizi</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {EQUIPMENT_CARDS.map((eq) => (
            <Link
              key={eq.id}
              to={`/equipment/${eq.id}`}
              className="bg-white rounded-xl border border-gray-200 p-5 hover:shadow-lg hover:border-primary-300 transition-all group"
            >
              <div className={`w-12 h-12 ${eq.color} rounded-lg flex items-center justify-center mb-4`}>
                <eq.icon className="w-6 h-6 text-white" />
              </div>
              <h3 className="font-semibold text-gray-900 group-hover:text-primary-600">
                {eq.name}
              </h3>
              <p className="text-sm text-gray-500 mt-1">{eq.description}</p>
              <div className="flex items-center justify-between mt-4">
                <span className="text-xs text-gray-400">{eq.stats}</span>
                <ArrowRight className="w-4 h-4 text-gray-400 group-hover:text-primary-500 group-hover:translate-x-1 transition-transform" />
              </div>
            </Link>
          ))}
        </div>
      </div>

      {/* Factory Analysis Promo */}
      <Card>
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-lg font-semibold text-gray-900">🏭 Fabrika Analizi</h3>
            <p className="text-gray-600 mt-1">
              Tüm ekipmanlarınızı bir arada analiz edin, fabrika genelinde exergy akışını görün
            </p>
          </div>
          <Link
            to="/factory"
            className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors"
          >
            Yeni Proje
          </Link>
        </div>
      </Card>
    </div>
  );
};

export default Dashboard;
```

### 3.8 API Service Güncelleme

`/frontend/src/services/api.js` güncellemeler:

```javascript
// Yeni endpoint'ler ekle

export const getEquipmentTypes = async () => {
  const response = await api.get('/equipment-types');
  return response.data;
};

export const getEquipmentSubtypes = async (equipmentType) => {
  const response = await api.get(`/equipment-types/${equipmentType}/subtypes`);
  return response.data;
};

// analyzeCompressor -> analyzeEquipment olarak güncelle
export const analyzeEquipment = async (equipmentType, subtype, parameters) => {
  const response = await api.post('/analyze', {
    equipment_type: equipmentType,
    subtype: subtype,
    parameters,
  });
  return response.data;
};
```

---

## 🏭 BÖLÜM 4: Fabrika Analizi (Temel)

### 4.1 Veri Modeli

```javascript
// Fabrika projesi
{
  id: "factory_001",
  name: "Örnek Tekstil Fabrikası",
  created_at: "2026-02-01",
  equipment: [
    {
      id: "eq_001",
      type: "compressor",
      subtype: "screw",
      name: "Ana Kompresör",
      parameters: {...},
      analysis_result: {...}  // null if not analyzed
    },
    {
      id: "eq_002",
      type: "boiler",
      subtype: "steam_firetube",
      name: "Buhar Kazanı #1",
      parameters: {...},
      analysis_result: null
    }
  ],
  summary: {
    total_power_kW: 245,
    total_exergy_loss_kW: 89,
    factory_exergy_efficiency: 0.42,
    total_annual_cost_eur: 45000
  }
}
```

### 4.2 Backend Endpoint

`/api/routes/factory.py`:

```python
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class EquipmentItem(BaseModel):
    id: str
    type: str
    subtype: str
    name: str
    parameters: dict
    analysis_result: Optional[dict] = None

class FactoryProject(BaseModel):
    id: Optional[str] = None
    name: str
    equipment: List[EquipmentItem] = []

# In-memory storage (sonra database eklenebilir)
projects = {}

@router.post("/factory/projects")
def create_project(project: FactoryProject):
    """Yeni fabrika projesi oluştur"""
    import uuid
    project.id = str(uuid.uuid4())[:8]
    projects[project.id] = project.dict()
    return {"success": True, "project": projects[project.id]}

@router.get("/factory/projects/{project_id}")
def get_project(project_id: str):
    """Fabrika projesini getir"""
    if project_id not in projects:
        return {"success": False, "error": "Project not found"}
    return {"success": True, "project": projects[project_id]}

@router.post("/factory/projects/{project_id}/analyze")
async def analyze_factory(project_id: str):
    """Fabrika genelinde analiz çalıştır"""
    if project_id not in projects:
        return {"success": False, "error": "Project not found"}
    
    project = projects[project_id]
    
    # Her ekipmanı analiz et
    total_power = 0
    total_loss = 0
    total_cost = 0
    
    for eq in project["equipment"]:
        if eq.get("analysis_result"):
            metrics = eq["analysis_result"].get("metrics", {})
            total_power += metrics.get("exergy_input_kW", 0)
            total_loss += metrics.get("exergy_destroyed_kW", 0)
            total_cost += metrics.get("annual_cost_eur", 0)
    
    # Fabrika özeti
    project["summary"] = {
        "total_power_kW": total_power,
        "total_exergy_loss_kW": total_loss,
        "factory_exergy_efficiency": (total_power - total_loss) / total_power if total_power > 0 else 0,
        "total_annual_cost_eur": total_cost,
    }
    
    projects[project_id] = project
    
    return {"success": True, "project": project}
```

---

## ✅ BÖLÜM 5: Uygulama Sırası

**ADIM 1: Knowledge Base Reorganizasyonu**
```bash
# Bash script'i çalıştır
bash reorganize_knowledge.sh
# Doğrula
tree knowledge -L 2
```

**ADIM 2: Backend Güncellemeleri**
1. `equipment_registry.py` oluştur
2. `routes/analysis.py` güncelle
3. `routes/factory.py` oluştur
4. `main.py` güncelle (factory router ekle)
5. SKILL dosyasını güncelle
6. Test et

**ADIM 3: Frontend Güncellemeleri**
1. `react-router-dom` yükle
2. `Sidebar.jsx` oluştur
3. `Layout.jsx` güncelle
4. `App.jsx` routing ekle
5. `pages/Dashboard.jsx` oluştur
6. `pages/EquipmentAnalysis.jsx` oluştur
7. `api.js` güncelle
8. `useAnalysis.js` güncelle
9. Build ve test

**ADIM 4: Fabrika Analizi (Temel)**
1. Backend endpoint'leri
2. Frontend sayfaları
3. Test

---

## 🧪 Test Kontrol Listesi

- [ ] Knowledge base yeni yapıda, tüm dosyalar yerinde
- [ ] Backend `/equipment-types` endpoint çalışıyor
- [ ] Backend `/equipment-types/{type}/subtypes` çalışıyor
- [ ] Backend `/analyze` tüm ekipman tipleri için çalışıyor
- [ ] Frontend sidebar görünüyor
- [ ] Frontend routing çalışıyor (`/`, `/equipment/compressor`, vb.)
- [ ] Kompresör analizi eski gibi çalışıyor
- [ ] Kazan analizi çalışıyor (engine eklendiğinde)
- [ ] Chiller analizi çalışıyor (engine eklendiğinde)
- [ ] Pompa analizi çalışıyor (engine eklendiğinde)
- [ ] AI yorumlama tüm ekipman tipleri için çalışıyor

---

**Bu brief ExergyLab büyük refactoring için tek kaynak noktasıdır.**
