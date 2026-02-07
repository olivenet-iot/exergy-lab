# Brief 22: Exergoeconomic Analysis — Maliyet Boyutu

> **Claude Code için:** Bu brief'i oku ve uygula. Mevcut exergy analizine maliyet boyutu ekle. Exergy yıkımının maliyeti, exergoekonomik faktör (f), göreceli maliyet farkı (r) hesapla.

---

## 🎯 Hedef

**Mevcut durum:** Exergy analizi sadece termodinamik — kW, verim, yıkım. Maliyet yok.

**Hedef:** Her ekipman analizi artık şunları da hesaplayacak:
- **Ċ_D** — Exergy yıkımının maliyet oranı (€/h)
- **f** — Exergoekonomik faktör (yatırım vs yakıt maliyeti dengesi)
- **r** — Göreceli maliyet farkı (ürün vs yakıt maliyet artışı)
- **Yıllık maliyet etkisi** — Daha doğru €/yıl hesabı

**Scope:** 4 engine (compressor, boiler, chiller, pump) + frontend gösterimi. Factory aggregation sonra.

---

## 📚 Exergoekonomik Temel Kavramlar

### Temel Formüller

```
Exergy Cost Rate:
  Ċ = c × Ė
  
Exergy Destruction Cost:
  Ċ_D = c_F × Ė_D
  
Exergoeconomic Factor:
  f = Ż / (Ż + Ċ_D)
  
Relative Cost Difference:
  r = (c_P - c_F) / c_F
  
Capital Cost Rate:
  Ż = Z_total × CRF / (τ × 3600)
  CRF = i(1+i)^n / ((1+i)^n - 1)
```

### Değişkenler

| Sembol | Açıklama | Birim |
|--------|----------|-------|
| Ċ | Exergy maliyet oranı | €/h |
| c | Spesifik exergy maliyeti | €/GJ |
| Ė | Exergy akış oranı | kW |
| Ė_D | Exergy yıkım oranı | kW |
| Ż | Yatırım maliyet oranı | €/h |
| Z_total | Toplam ekipman yatırımı | € |
| CRF | Capital Recovery Factor | - |
| i | Faiz oranı (discount rate) | - |
| n | Ekipman ömrü | yıl |
| τ | Yıllık çalışma saati | h/yıl |
| c_F | Yakıt (giriş) exergy maliyeti | €/GJ |
| c_P | Ürün (çıkış) exergy maliyeti | €/GJ |
| f | Exergoekonomik faktör | - |
| r | Göreceli maliyet farkı | - |

---

## ⚠️ OTONOM YETKİ

1. Brief'teki görevleri tamamla
2. Mevcut analiz sonuçlarını BOZMA — ek field'lar ekle
3. 431 testi BOZMA
4. Yeni paket EKLEME (yok)
5. Frontend'de yeni tab/section ekle

---

## 📋 Adım 0: Mevcut Durumu Anla

```bash
# 1. Compressor engine — mevcut analiz yapısı
cat engine/compressor.py | head -150

# 2. Boiler engine
cat engine/boiler.py | head -150

# 3. Chiller engine
cat engine/chiller.py | head -150

# 4. Pump engine
cat engine/pump.py | head -150

# 5. Core utils — mevcut yardımcı fonksiyonlar
cat engine/core.py

# 6. Mevcut API response yapısı
cat api/routes/equipment.py | head -100

# 7. Frontend results — mevcut metrik kartları
cat frontend/src/components/dashboard/MetricBar.jsx
cat frontend/src/components/dashboard/FlowTab.jsx

# 8. Exergoeconomic knowledge dosyaları
ls knowledge/exergoeconomic/
cat knowledge/exergoeconomic/INDEX.md 2>/dev/null || echo "Check path"
```

---

## 📦 Dosya Yapısı

```
engine/
├── core.py                 # GÜNCELLEME — exergoeconomic utils
├── compressor.py           # GÜNCELLEME — exergoeconomic hesap
├── boiler.py              # GÜNCELLEME — exergoeconomic hesap
├── chiller.py             # GÜNCELLEME — exergoeconomic hesap
├── pump.py                # GÜNCELLEME — exergoeconomic hesap
└── exergoeconomic.py      # YENİ — ortak hesaplama fonksiyonları

api/
└── schemas/
    └── equipment.py        # GÜNCELLEME — yeni input/output fields

frontend/src/
├── components/
│   └── dashboard/
│       └── FlowTab.jsx     # GÜNCELLEME — exergoeconomic section
│       └── MetricBar.jsx   # GÜNCELLEME — cost metrics (opsiyonel)
└── pages/
    └── EquipmentAnalysis.jsx  # Parametre formu (cost inputs)
```

---

## 📦 Adım 1: Exergoeconomic Engine Module

### `engine/exergoeconomic.py` (YENİ)

```python
"""
Exergoeconomic analysis calculations.

Provides cost-based analysis functions for all equipment types.
Based on SPECO method (Specific Exergy Costing).
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class ExergoeconomicInput:
    """Common economic input parameters."""
    # Energy costs
    electricity_cost_eur_kwh: float = 0.10        # €/kWh electricity
    fuel_cost_eur_kwh: float = 0.05              # €/kWh fuel (gas, oil, etc.)
    
    # Equipment costs
    equipment_cost_eur: float = 10000.0          # € total equipment cost
    installation_factor: float = 1.4              # Installation multiplier
    
    # Economic parameters
    interest_rate: float = 0.08                   # 8% discount rate
    equipment_lifetime_years: int = 15            # years
    operating_hours_year: int = 8000              # h/year
    
    # Maintenance
    maintenance_factor: float = 0.02              # 2% of capital/year


@dataclass
class ExergoeconomicResult:
    """Exergoeconomic analysis results."""
    # Cost rates (€/h)
    Z_dot: float                    # Capital + O&M cost rate
    C_dot_fuel: float               # Fuel exergy cost rate
    C_dot_product: float            # Product exergy cost rate
    C_dot_destruction: float        # Exergy destruction cost rate
    C_dot_loss: float               # Exergy loss cost rate
    
    # Specific costs (€/GJ)
    c_fuel: float                   # Fuel specific exergy cost
    c_product: float                # Product specific exergy cost
    
    # Exergoeconomic indicators
    f_factor: float                 # f = Z / (Z + C_D) — exergoeconomic factor
    r_factor: float                 # r = (c_P - c_F) / c_F — relative cost difference
    
    # Annual costs (€/year)
    annual_fuel_cost: float
    annual_destruction_cost: float
    annual_total_cost: float
    
    # For display
    destruction_cost_share_pct: float  # C_D / (Z + C_D) as percentage


def calculate_capital_recovery_factor(interest_rate: float, lifetime_years: int) -> float:
    """
    Calculate Capital Recovery Factor (CRF).
    
    CRF = i(1+i)^n / ((1+i)^n - 1)
    
    Args:
        interest_rate: Annual interest rate (e.g., 0.08 for 8%)
        lifetime_years: Equipment lifetime in years
        
    Returns:
        CRF value
    """
    i = interest_rate
    n = lifetime_years
    
    if i == 0:
        return 1 / n
    
    return (i * (1 + i)**n) / ((1 + i)**n - 1)


def calculate_capital_cost_rate(
    equipment_cost_eur: float,
    installation_factor: float,
    maintenance_factor: float,
    interest_rate: float,
    lifetime_years: int,
    operating_hours_year: int
) -> float:
    """
    Calculate capital + O&M cost rate (Ż).
    
    Ż = (Z_total × CRF + Z_total × φ_OM) / τ
    
    Args:
        equipment_cost_eur: Equipment purchase cost (€)
        installation_factor: Installation multiplier (typically 1.2-1.6)
        maintenance_factor: O&M as fraction of capital (typically 0.02-0.06)
        interest_rate: Discount rate
        lifetime_years: Equipment lifetime
        operating_hours_year: Annual operating hours
        
    Returns:
        Ż in €/h
    """
    # Total installed cost
    Z_total = equipment_cost_eur * installation_factor
    
    # Capital recovery factor
    CRF = calculate_capital_recovery_factor(interest_rate, lifetime_years)
    
    # Annual capital cost
    annual_capital = Z_total * CRF
    
    # Annual O&M cost
    annual_om = Z_total * maintenance_factor
    
    # Cost rate (€/h)
    Z_dot = (annual_capital + annual_om) / operating_hours_year
    
    return Z_dot


def kwh_to_gj(kwh: float) -> float:
    """Convert kWh to GJ. 1 kWh = 0.0036 GJ"""
    return kwh * 0.0036


def eur_per_kwh_to_eur_per_gj(eur_kwh: float) -> float:
    """Convert €/kWh to €/GJ. €/kWh × (1/0.0036) = €/GJ"""
    return eur_kwh / 0.0036


def calculate_exergoeconomic(
    # Exergy flows (kW)
    exergy_fuel_kW: float,
    exergy_product_kW: float,
    exergy_destruction_kW: float,
    exergy_loss_kW: float = 0.0,
    
    # Economic inputs
    fuel_cost_eur_kwh: float = 0.10,
    equipment_cost_eur: float = 10000.0,
    installation_factor: float = 1.4,
    maintenance_factor: float = 0.02,
    interest_rate: float = 0.08,
    lifetime_years: int = 15,
    operating_hours_year: int = 8000,
) -> ExergoeconomicResult:
    """
    Perform exergoeconomic analysis for any component.
    
    Uses SPECO method:
    - Fuel rule: Fuel exergy carries the cost of purchased resources
    - Product rule: Product exergy carries fuel cost + component cost
    
    Args:
        exergy_fuel_kW: Input/fuel exergy rate (kW)
        exergy_product_kW: Output/product exergy rate (kW)
        exergy_destruction_kW: Exergy destruction rate (kW)
        exergy_loss_kW: Exergy loss rate (kW)
        fuel_cost_eur_kwh: Cost of fuel/input energy (€/kWh)
        equipment_cost_eur: Equipment cost (€)
        installation_factor: Installation multiplier
        maintenance_factor: O&M fraction
        interest_rate: Discount rate
        lifetime_years: Equipment lifetime (years)
        operating_hours_year: Annual operating hours
        
    Returns:
        ExergoeconomicResult with all cost metrics
    """
    # Capital cost rate (€/h)
    Z_dot = calculate_capital_cost_rate(
        equipment_cost_eur=equipment_cost_eur,
        installation_factor=installation_factor,
        maintenance_factor=maintenance_factor,
        interest_rate=interest_rate,
        lifetime_years=lifetime_years,
        operating_hours_year=operating_hours_year
    )
    
    # Specific fuel exergy cost (€/GJ)
    c_fuel = eur_per_kwh_to_eur_per_gj(fuel_cost_eur_kwh)
    
    # Fuel exergy cost rate (€/h)
    # Ċ_F = c_F × Ė_F  (convert kW to GJ/h: kW × 0.0036)
    C_dot_fuel = c_fuel * exergy_fuel_kW * 0.0036
    
    # Exergy destruction cost rate (€/h)
    # Ċ_D = c_F × Ė_D
    C_dot_destruction = c_fuel * exergy_destruction_kW * 0.0036
    
    # Exergy loss cost rate (€/h)
    C_dot_loss = c_fuel * exergy_loss_kW * 0.0036
    
    # Product exergy cost rate (€/h)
    # Cost balance: Ċ_F + Ż = Ċ_P + Ċ_L (assuming losses carry fuel cost)
    # Ċ_P = Ċ_F + Ż - Ċ_L
    C_dot_product = C_dot_fuel + Z_dot - C_dot_loss
    
    # Specific product exergy cost (€/GJ)
    if exergy_product_kW > 0:
        c_product = C_dot_product / (exergy_product_kW * 0.0036)
    else:
        c_product = 0.0
    
    # Exergoeconomic factor
    # f = Ż / (Ż + Ċ_D)
    denominator = Z_dot + C_dot_destruction
    if denominator > 0:
        f_factor = Z_dot / denominator
    else:
        f_factor = 0.0
    
    # Relative cost difference
    # r = (c_P - c_F) / c_F
    if c_fuel > 0:
        r_factor = (c_product - c_fuel) / c_fuel
    else:
        r_factor = 0.0
    
    # Destruction cost share (%)
    if denominator > 0:
        destruction_cost_share_pct = (C_dot_destruction / denominator) * 100
    else:
        destruction_cost_share_pct = 0.0
    
    # Annual costs (€/year)
    annual_fuel_cost = C_dot_fuel * operating_hours_year
    annual_destruction_cost = C_dot_destruction * operating_hours_year
    annual_total_cost = (C_dot_fuel + Z_dot) * operating_hours_year
    
    return ExergoeconomicResult(
        Z_dot=round(Z_dot, 4),
        C_dot_fuel=round(C_dot_fuel, 4),
        C_dot_product=round(C_dot_product, 4),
        C_dot_destruction=round(C_dot_destruction, 4),
        C_dot_loss=round(C_dot_loss, 4),
        c_fuel=round(c_fuel, 2),
        c_product=round(c_product, 2),
        f_factor=round(f_factor, 3),
        r_factor=round(r_factor, 3),
        annual_fuel_cost=round(annual_fuel_cost, 2),
        annual_destruction_cost=round(annual_destruction_cost, 2),
        annual_total_cost=round(annual_total_cost, 2),
        destruction_cost_share_pct=round(destruction_cost_share_pct, 1)
    )


def interpret_f_factor(f: float) -> str:
    """
    Interpret exergoeconomic factor.
    
    f > 0.5: Component improvement should focus on reducing capital cost
    f < 0.5: Component improvement should focus on increasing efficiency
    """
    if f > 0.7:
        return "Yatırım maliyeti dominant — daha ucuz ekipman arayın"
    elif f > 0.5:
        return "Yatırım maliyeti biraz yüksek — maliyet optimizasyonu düşünün"
    elif f > 0.3:
        return "Dengeli — hem verim hem maliyet önemli"
    else:
        return "Verim dominant — ekipman verimliliğini artırın"


def interpret_r_factor(r: float) -> str:
    """
    Interpret relative cost difference.
    
    High r: Large cost increase from fuel to product — improvement potential
    Low r: Efficient cost conversion
    """
    if r > 1.0:
        return "Yüksek maliyet artışı — iyileştirme potansiyeli yüksek"
    elif r > 0.5:
        return "Orta maliyet artışı — iyileştirme değerlendirilmeli"
    elif r > 0.25:
        return "Kabul edilebilir maliyet artışı"
    else:
        return "Düşük maliyet artışı — verimli çalışıyor"
```

---

## 📦 Adım 2: Input Schema Güncellemesi

### `api/schemas/equipment.py` — Yeni Cost Fields

Her ekipman input schema'sına opsiyonel ekonomik parametreler ekle:

```python
# Mevcut CompressorInput'a ekle:
class CompressorInput(BaseModel):
    # ... mevcut alanlar ...
    
    # Exergoeconomic parameters (optional)
    electricity_cost_eur_kwh: float = Field(0.10, ge=0, description="Elektrik maliyeti (€/kWh)")
    equipment_cost_eur: float = Field(10000, ge=0, description="Ekipman maliyeti (€)")
    installation_factor: float = Field(1.4, ge=1.0, le=3.0, description="Kurulum faktörü")
    maintenance_factor: float = Field(0.02, ge=0, le=0.2, description="Bakım faktörü")
    interest_rate: float = Field(0.08, ge=0, le=0.3, description="Faiz oranı")
    equipment_lifetime_years: int = Field(15, ge=1, le=50, description="Ekipman ömrü (yıl)")


# Benzer şekilde BoilerInput, ChillerInput, PumpInput'a da ekle
# Boiler için: fuel_cost_eur_kwh (yakıt maliyeti)
# Chiller için: electricity_cost_eur_kwh
# Pump için: electricity_cost_eur_kwh
```

---

## 📦 Adım 3: Engine Güncellemeleri

### `engine/compressor.py` — Exergoeconomic Integration

```python
# Import ekle:
from engine.exergoeconomic import calculate_exergoeconomic, ExergoeconomicResult

# analyze_compressor fonksiyonuna ekonomik parametreler ekle:
def analyze_compressor(
    # ... mevcut parametreler ...
    
    # Ekonomik parametreler (yeni)
    electricity_cost_eur_kwh: float = 0.10,
    equipment_cost_eur: float = 10000.0,
    installation_factor: float = 1.4,
    maintenance_factor: float = 0.02,
    interest_rate: float = 0.08,
    equipment_lifetime_years: int = 15,
) -> CompressorResult:
    
    # ... mevcut hesaplamalar ...
    
    # Exergoeconomic hesaplama (YENİ)
    exergoeconomic = calculate_exergoeconomic(
        exergy_fuel_kW=shaft_power,  # Kompresör için fuel = elektrik
        exergy_product_kW=result.exergy_output_kW,
        exergy_destruction_kW=result.exergy_destroyed_kW,
        exergy_loss_kW=0,  # Kompresörde kayıp ≈ 0 varsayımı
        fuel_cost_eur_kwh=electricity_cost_eur_kwh,
        equipment_cost_eur=equipment_cost_eur,
        installation_factor=installation_factor,
        maintenance_factor=maintenance_factor,
        interest_rate=interest_rate,
        lifetime_years=equipment_lifetime_years,
        operating_hours_year=operating_hours_year
    )
    
    # Result'a exergoeconomic ekle
    result.exergoeconomic = exergoeconomic
    
    return result


# CompressorResult dataclass'ına ekle:
@dataclass
class CompressorResult:
    # ... mevcut alanlar ...
    
    # Exergoeconomic (yeni)
    exergoeconomic: Optional[ExergoeconomicResult] = None
```

### Diğer Engine'ler için Benzer Pattern

**Boiler:**
- Fuel = yakıt exergy'si
- Product = buhar/su exergy'si
- fuel_cost = yakıt maliyeti (doğalgaz, kömür, vb.)

**Chiller:**
- Fuel = elektrik (vapor compression) veya ısı (absorption)
- Product = soğutma exergy'si

**Pump:**
- Fuel = elektrik
- Product = hidrolik exergy

---

## 📦 Adım 4: API Response Güncellemesi

### `api/routes/equipment.py` — to_api_dict Güncelleme

```python
# to_api_dict fonksiyonuna exergoeconomic ekle:
def result_to_api_dict(result):
    data = {
        # ... mevcut alanlar ...
    }
    
    # Exergoeconomic varsa ekle
    if hasattr(result, 'exergoeconomic') and result.exergoeconomic:
        eco = result.exergoeconomic
        data['exergoeconomic'] = {
            'Z_dot_eur_h': eco.Z_dot,
            'C_dot_fuel_eur_h': eco.C_dot_fuel,
            'C_dot_product_eur_h': eco.C_dot_product,
            'C_dot_destruction_eur_h': eco.C_dot_destruction,
            'c_fuel_eur_gj': eco.c_fuel,
            'c_product_eur_gj': eco.c_product,
            'f_factor': eco.f_factor,
            'r_factor': eco.r_factor,
            'annual_fuel_cost_eur': eco.annual_fuel_cost,
            'annual_destruction_cost_eur': eco.annual_destruction_cost,
            'annual_total_cost_eur': eco.annual_total_cost,
            'destruction_cost_share_pct': eco.destruction_cost_share_pct,
        }
    
    return data
```

---

## 📦 Adım 5: Frontend Updates

### `frontend/src/components/forms/ParameterForm.jsx` — Cost Inputs

Forma ekonomik parametre inputları ekle (collapsible section):

```jsx
{/* Ekonomik Parametreler (collapsible) */}
<details className="mt-4">
  <summary className="cursor-pointer text-sm font-medium text-slate-600">
    💰 Ekonomik Parametreler (opsiyonel)
  </summary>
  <div className="mt-2 space-y-3 pl-4 border-l-2 border-slate-200">
    <FormField
      label="Elektrik Maliyeti"
      name="electricity_cost_eur_kwh"
      type="number"
      step="0.01"
      unit="€/kWh"
      defaultValue={0.10}
    />
    <FormField
      label="Ekipman Maliyeti"
      name="equipment_cost_eur"
      type="number"
      unit="€"
      defaultValue={10000}
    />
    {/* ... diğer ekonomik alanlar ... */}
  </div>
</details>
```

### `frontend/src/components/dashboard/FlowTab.jsx` — Exergoeconomic Section

```jsx
{/* Exergoeconomic Analysis Section (yeni) */}
{result.exergoeconomic && (
  <Card className="mt-6">
    <h3 className="text-lg font-semibold mb-4">💰 Exergoekonomik Analiz</h3>
    
    <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
      {/* f-factor */}
      <div className="bg-slate-50 rounded-lg p-4">
        <div className="text-xs text-slate-500 uppercase">Exergoekonomik Faktör (f)</div>
        <div className="text-2xl font-mono font-bold text-cyan-600">
          {result.exergoeconomic.f_factor.toFixed(2)}
        </div>
        <div className="text-xs text-slate-600 mt-1">
          {result.exergoeconomic.f_factor > 0.5 
            ? 'Yatırım maliyeti dominant' 
            : 'Verim iyileştirmesi öncelikli'}
        </div>
      </div>
      
      {/* r-factor */}
      <div className="bg-slate-50 rounded-lg p-4">
        <div className="text-xs text-slate-500 uppercase">Göreceli Maliyet Farkı (r)</div>
        <div className="text-2xl font-mono font-bold text-amber-600">
          {(result.exergoeconomic.r_factor * 100).toFixed(0)}%
        </div>
      </div>
      
      {/* Destruction Cost */}
      <div className="bg-red-50 rounded-lg p-4">
        <div className="text-xs text-slate-500 uppercase">Yıkım Maliyeti</div>
        <div className="text-2xl font-mono font-bold text-red-600">
          €{result.exergoeconomic.annual_destruction_cost_eur.toLocaleString()}/yıl
        </div>
        <div className="text-xs text-slate-600 mt-1">
          Toplam maliyetin %{result.exergoeconomic.destruction_cost_share_pct}'i
        </div>
      </div>
      
      {/* Total Cost */}
      <div className="bg-slate-50 rounded-lg p-4">
        <div className="text-xs text-slate-500 uppercase">Toplam İşletme Maliyeti</div>
        <div className="text-2xl font-mono font-bold">
          €{result.exergoeconomic.annual_total_cost_eur.toLocaleString()}/yıl
        </div>
      </div>
    </div>
    
    {/* Cost Breakdown Bar */}
    <div className="mt-4">
      <div className="text-sm text-slate-600 mb-2">Maliyet Dağılımı</div>
      <div className="h-4 rounded-full overflow-hidden flex">
        <div 
          className="bg-cyan-500"
          style={{ width: `${result.exergoeconomic.f_factor * 100}%` }}
          title="Yatırım + Bakım"
        />
        <div 
          className="bg-red-500"
          style={{ width: `${result.exergoeconomic.destruction_cost_share_pct}%` }}
          title="Exergy Yıkımı"
        />
      </div>
      <div className="flex justify-between text-xs text-slate-500 mt-1">
        <span>Yatırım+Bakım (Ż)</span>
        <span>Exergy Yıkımı (Ċ_D)</span>
      </div>
    </div>
  </Card>
)}
```

---

## 📦 Adım 6: Test Ekleme

### `tests/test_exergoeconomic.py` (YENİ)

```python
"""
Tests for exergoeconomic analysis module.
"""
import pytest
from engine.exergoeconomic import (
    calculate_capital_recovery_factor,
    calculate_capital_cost_rate,
    calculate_exergoeconomic,
    eur_per_kwh_to_eur_per_gj
)


class TestCapitalRecoveryFactor:
    def test_basic_crf(self):
        """CRF with 8% interest, 15 years."""
        crf = calculate_capital_recovery_factor(0.08, 15)
        assert 0.11 < crf < 0.12  # Should be ~0.1168

    def test_zero_interest(self):
        """CRF with 0% interest."""
        crf = calculate_capital_recovery_factor(0.0, 10)
        assert crf == 0.1


class TestCapitalCostRate:
    def test_basic_calculation(self):
        """Basic Z_dot calculation."""
        Z_dot = calculate_capital_cost_rate(
            equipment_cost_eur=10000,
            installation_factor=1.4,
            maintenance_factor=0.02,
            interest_rate=0.08,
            lifetime_years=15,
            operating_hours_year=8000
        )
        # Should be around 0.25 €/h
        assert 0.2 < Z_dot < 0.4


class TestExergoeconomicCalculation:
    def test_compressor_example(self):
        """Test with typical compressor values."""
        result = calculate_exergoeconomic(
            exergy_fuel_kW=100,      # 100 kW input
            exergy_product_kW=60,    # 60 kW output (60% efficiency)
            exergy_destruction_kW=40, # 40 kW destroyed
            fuel_cost_eur_kwh=0.10,
            equipment_cost_eur=20000,
            operating_hours_year=8000
        )
        
        # Basic checks
        assert result.C_dot_destruction > 0
        assert 0 < result.f_factor < 1
        assert result.r_factor > 0
        assert result.annual_destruction_cost > 0
        
    def test_f_factor_interpretation(self):
        """f > 0.5 means capital dominant."""
        # High equipment cost, low destruction
        result = calculate_exergoeconomic(
            exergy_fuel_kW=100,
            exergy_product_kW=95,  # Very efficient
            exergy_destruction_kW=5,
            equipment_cost_eur=100000,  # Expensive
            fuel_cost_eur_kwh=0.05      # Cheap fuel
        )
        assert result.f_factor > 0.5  # Capital should dominate


class TestUnitConversion:
    def test_eur_kwh_to_gj(self):
        """€0.10/kWh = €27.78/GJ"""
        result = eur_per_kwh_to_eur_per_gj(0.10)
        assert 27 < result < 28
```

---

## 📋 Uygulama Sırası

### Faz 1: Keşif
1. Mevcut engine yapılarını oku
2. Mevcut API response yapısını anla
3. Knowledge base'deki exergoeconomic dosyalarına bak

### Faz 2: Engine Module
4. `engine/exergoeconomic.py` — Yeni modül oluştur
5. Test yaz: `tests/test_exergoeconomic.py`

### Faz 3: Engine Integration
6. `engine/compressor.py` — Exergoeconomic integration
7. `engine/boiler.py` — Exergoeconomic integration
8. `engine/chiller.py` — Exergoeconomic integration
9. `engine/pump.py` — Exergoeconomic integration

### Faz 4: API Updates
10. `api/schemas/equipment.py` — Cost input fields (opsiyonel, default değerli)
11. `api/routes/equipment.py` — Response'a exergoeconomic ekle

### Faz 5: Frontend
12. `frontend/src/components/forms/ParameterForm.jsx` — Cost inputs (collapsible)
13. `frontend/src/components/dashboard/FlowTab.jsx` — Exergoeconomic section

### Faz 6: Verification
14. `pytest tests/ -v` — Yeni testler dahil tümü geçmeli
15. `cd frontend && npx vite build`
16. Manual test: analiz yap, exergoeconomic sonuçları gör
17. `git add -A && git commit && git push`

---

## ✅ Tamamlanma Kriterleri

- [ ] `engine/exergoeconomic.py` modülü oluşturuldu
- [ ] 4 engine'e exergoeconomic integration (compressor, boiler, chiller, pump)
- [ ] API response'a exergoeconomic data eklendi
- [ ] Frontend'de ekonomik parametre inputları (collapsible)
- [ ] Frontend'de exergoeconomic sonuç gösterimi (FlowTab)
- [ ] f-factor ve r-factor yorumları
- [ ] Yıkım maliyeti (€/yıl) hesabı
- [ ] Maliyet dağılımı bar chart
- [ ] Yeni testler yazıldı ve geçti
- [ ] Mevcut 431 test hâlâ geçiyor
- [ ] `git add -A && git commit && git push`

---

## 📊 Beklenen Sonuç

| Metrik | Önceki | Sonrası |
|--------|--------|---------|
| Maliyet analizi | Basit €/yıl | f-factor, r-factor, Ċ_D |
| Karar desteği | "Verim düşük" | "Yatırım maliyeti dominant, daha ucuz ekipman arayın" |
| Yıkım maliyeti | Yok | €/yıl + payı (%) |
| İyileştirme yönü | Belirsiz | f>0.5: maliyet, f<0.5: verim |
