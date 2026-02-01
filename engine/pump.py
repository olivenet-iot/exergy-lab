"""
ExergyLab - Pump Exergy Analysis

Pompa exergy hesaplamalari.
Santrifuj, pozitif deplasman ve diger pompa tipleri icin.
"""

from dataclasses import dataclass
from typing import Optional
import math

from .core import DeadState, ExergyResult, celsius_to_kelvin


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

GRAVITY = 9.81  # m/s^2


# ---------------------------------------------------------------------------
# Input dataclass
# ---------------------------------------------------------------------------

@dataclass
class PumpInput:
    """Pompa analizi icin giris verileri"""

    # Zorunlu
    motor_power_kW: float           # Motor elektrik gucu [kW]
    flow_rate_m3_h: float           # Debi [m3/h]
    total_head_m: float             # Toplam basma yuksekligi [m]

    # Opsiyonel
    fluid_density_kg_m3: float = 1000.0   # Akiskan yogunlugu [kg/m3]
    pump_type: str = "centrifugal"         # centrifugal, positive_displacement, submersible, etc.
    control_method: str = "none"           # none, throttle, vsd, bypass
    throttle_loss_pct: float = 0.0         # Vana kaybi [%]
    has_vsd: bool = False                  # VSD var mi?
    motor_efficiency_pct: Optional[float] = None   # Motor verimi [%]
    pump_efficiency_pct: Optional[float] = None    # Pompa verimi [%]
    ambient_temp_C: Optional[float] = None
    operating_hours: float = 6000
    electricity_price_eur_kwh: float = 0.12

    def __post_init__(self):
        if self.ambient_temp_C is None:
            self.ambient_temp_C = 25.0
        if self.motor_efficiency_pct is None:
            defaults = {
                'centrifugal': 93.0,
                'positive_displacement': 91.0,
                'submersible': 88.0,
                'vertical_turbine': 92.0,
                'booster': 90.0,
                'vacuum': 85.0,
            }
            self.motor_efficiency_pct = defaults.get(self.pump_type, 93.0)
        if self.pump_efficiency_pct is None:
            defaults = {
                'centrifugal': 78.0,
                'positive_displacement': 82.0,
                'submersible': 70.0,
                'vertical_turbine': 80.0,
                'booster': 75.0,
                'vacuum': 65.0,
            }
            self.pump_efficiency_pct = defaults.get(self.pump_type, 78.0)


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class PumpResult(ExergyResult):
    """Pompa analizi sonuclari"""

    hydraulic_power_kW: Optional[float] = None
    motor_loss_kW: Optional[float] = None
    pump_loss_kW: Optional[float] = None
    throttle_loss_kW: Optional[float] = None
    wire_to_water_efficiency_pct: Optional[float] = None
    vsd_savings_potential_kW: Optional[float] = None
    benchmark_comparison: Optional[str] = None

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            'hydraulic_power_kW': round(self.hydraulic_power_kW, 2) if self.hydraulic_power_kW else None,
            'motor_loss_kW': round(self.motor_loss_kW, 2) if self.motor_loss_kW else None,
            'pump_loss_kW': round(self.pump_loss_kW, 2) if self.pump_loss_kW else None,
            'throttle_loss_kW': round(self.throttle_loss_kW, 2) if self.throttle_loss_kW else None,
            'wire_to_water_efficiency_pct': round(self.wire_to_water_efficiency_pct, 1) if self.wire_to_water_efficiency_pct else None,
            'vsd_savings_potential_kW': round(self.vsd_savings_potential_kW, 2) if self.vsd_savings_potential_kW else None,
            'benchmark_comparison': self.benchmark_comparison,
        })
        return base

    def to_api_dict(self, pump_type: str = "centrifugal") -> dict:
        """API yanit formatina donusturur."""
        return {
            "exergy_input_kW": round(self.exergy_in_kW, 2),
            "exergy_output_kW": round(self.exergy_out_kW, 2),
            "exergy_destroyed_kW": round(self.exergy_destroyed_kW, 2),
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "hydraulic_power_kW": round(self.hydraulic_power_kW, 2) if self.hydraulic_power_kW else None,
            "motor_loss_kW": round(self.motor_loss_kW, 2) if self.motor_loss_kW else None,
            "pump_loss_kW": round(self.pump_loss_kW, 2) if self.pump_loss_kW else None,
            "throttle_loss_kW": round(self.throttle_loss_kW, 2) if self.throttle_loss_kW else None,
            "wire_to_water_efficiency_pct": round(self.wire_to_water_efficiency_pct, 1) if self.wire_to_water_efficiency_pct else None,
            "vsd_savings_potential_kW": round(self.vsd_savings_potential_kW, 2) if self.vsd_savings_potential_kW else None,
            "annual_loss_kWh": round(self.annual_loss_kWh, 0) if self.annual_loss_kWh else None,
            "annual_loss_EUR": round(self.annual_loss_EUR, 0) if self.annual_loss_EUR else None,
            "benchmark_comparison": self.benchmark_comparison,
            "benchmark_percentile": _calculate_percentile(self.exergy_efficiency_pct, pump_type),
            "comparison_text": _get_comparison_text(self.benchmark_comparison),
        }


# ---------------------------------------------------------------------------
# Analysis function
# ---------------------------------------------------------------------------

def analyze_pump(input_data: PumpInput, dead_state: DeadState = None) -> PumpResult:
    """
    Pompa exergy analizi yapar.

    Hesaplamalar:
    - P_hydraulic = rho * g * Q * H / 1000
    - Ex_in = P_electric (elektrik = saf exergy)
    - Ex_out = P_hydraulic
    - eta_ex = P_hydraulic / P_electric * 100

    Args:
        input_data: Pompa giris verileri
        dead_state: Dead state kosullari (opsiyonel)

    Returns:
        PumpResult: Analiz sonuclari
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)

    # Flow rate: m3/h -> m3/s
    Q_m3_s = input_data.flow_rate_m3_h / 3600.0

    # Hydraulic power: P_hyd = rho * g * Q * H / 1000
    P_hydraulic = (input_data.fluid_density_kg_m3 * GRAVITY * Q_m3_s * input_data.total_head_m) / 1000.0

    # Exergy input = electrical power (pure exergy)
    Ex_in = input_data.motor_power_kW

    # Motor loss
    motor_eff = input_data.motor_efficiency_pct / 100.0
    motor_shaft_power = Ex_in * motor_eff
    motor_loss = Ex_in - motor_shaft_power

    # Pump mechanical loss
    pump_eff = input_data.pump_efficiency_pct / 100.0
    pump_output = motor_shaft_power * pump_eff
    pump_loss = motor_shaft_power - pump_output

    # Throttle loss
    throttle_loss = Ex_in * (input_data.throttle_loss_pct / 100.0)

    # Exergy output = hydraulic power (useful work)
    Ex_out = P_hydraulic

    # Cap Ex_out at Ex_in
    if Ex_out > Ex_in:
        Ex_out = Ex_in * 0.95

    Ex_destroyed = Ex_in - Ex_out
    eta_ex = (Ex_out / Ex_in) * 100 if Ex_in > 0 else 0.0

    # Wire-to-water efficiency
    wire_to_water = (P_hydraulic / Ex_in) * 100 if Ex_in > 0 else 0.0

    # VSD savings potential (affinity laws)
    vsd_savings = 0.0
    if not input_data.has_vsd and input_data.control_method in ('throttle', 'bypass'):
        # Estimate: if throttling 20% of flow, VSD saves ~50% of throttle loss
        # Affinity law: P_new/P_old = (Q_new/Q_old)^3
        # Conservative estimate: 25% of motor power saveable
        vsd_savings = Ex_in * 0.25

    # Annual losses
    annual_loss_kWh = Ex_destroyed * input_data.operating_hours
    annual_loss_EUR = annual_loss_kWh * input_data.electricity_price_eur_kwh

    benchmark = _get_benchmark_comparison(eta_ex, input_data.pump_type)

    return PumpResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_out,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        hydraulic_power_kW=P_hydraulic,
        motor_loss_kW=motor_loss,
        pump_loss_kW=pump_loss,
        throttle_loss_kW=throttle_loss,
        wire_to_water_efficiency_pct=wire_to_water,
        vsd_savings_potential_kW=vsd_savings,
        benchmark_comparison=benchmark,
    )


# ---------------------------------------------------------------------------
# Sankey data
# ---------------------------------------------------------------------------

def generate_pump_sankey_data(result: PumpResult, pump_type: str = "centrifugal") -> dict:
    """
    Pompa Sankey diyagrami icin node ve link verisi olusturur.

    Nodes: Elektrik -> Motor -> Pompa -> Hidrolik Guc / Motor Kaybi / Pompa Kaybi / Throttle Kaybi
    """
    Ex_in = result.exergy_in_kW
    motor_loss = result.motor_loss_kW or 0.0
    pump_loss = result.pump_loss_kW or 0.0
    throttle_loss = result.throttle_loss_kW or 0.0
    hydraulic = result.hydraulic_power_kW or 0.0

    # Normalize to ensure energy balance
    total_out = hydraulic + motor_loss + pump_loss + throttle_loss
    other_loss = max(0.0, Ex_in - total_out)

    nodes = [
        {"id": 0, "name": "Elektrik Enerjisi", "name_en": "Electrical Energy"},
        {"id": 1, "name": "Motor", "name_en": "Motor"},
        {"id": 2, "name": "Pompa", "name_en": "Pump"},
        {"id": 3, "name": "Hidrolik Guc", "name_en": "Hydraulic Power"},
        {"id": 4, "name": "Motor Kaybi", "name_en": "Motor Loss"},
        {"id": 5, "name": "Pompa Kaybi", "name_en": "Pump Loss"},
        {"id": 6, "name": "Diger Kayiplar", "name_en": "Other Losses"},
    ]

    links = [
        {"source": 0, "target": 1, "value": round(Ex_in, 2), "label": "Elektrik Girisi"},
        {"source": 1, "target": 2, "value": round(Ex_in - motor_loss, 2), "label": "Saft Gucu"},
        {"source": 1, "target": 4, "value": round(motor_loss, 2), "label": "Motor Kaybi"},
        {"source": 2, "target": 3, "value": round(hydraulic, 2), "label": "Hidrolik Guc"},
        {"source": 2, "target": 5, "value": round(pump_loss, 2), "label": "Pompa Kaybi"},
        {"source": 2, "target": 6, "value": round(throttle_loss + other_loss, 2), "label": "Diger Kayiplar"},
    ]

    return {
        "nodes": nodes,
        "links": links,
        "summary": {
            "total_input_kW": round(Ex_in, 2),
            "useful_output_kW": round(hydraulic, 2),
            "recoverable_heat_kW": 0.0,
            "irreversibility_kW": round(Ex_in - hydraulic, 2),
            "efficiency_pct": round(result.exergy_efficiency_pct, 1),
        },
    }


# ---------------------------------------------------------------------------
# Recommendations
# ---------------------------------------------------------------------------

def get_pump_recommendations(result: PumpResult, input_data: PumpInput) -> list:
    """Pompa analiz sonuclarina gore iyilestirme onerileri."""
    recommendations = []

    # VSD recommendation
    if not input_data.has_vsd and result.vsd_savings_potential_kW and result.vsd_savings_potential_kW > 1:
        vsd_savings_eur = result.vsd_savings_potential_kW * input_data.operating_hours * input_data.electricity_price_eur_kwh
        vsd_cost = input_data.motor_power_kW * 100
        payback = vsd_cost / vsd_savings_eur if vsd_savings_eur > 0 else float('inf')
        recommendations.append({
            'type': 'vsd',
            'title': 'Degisken Hiz Surucusu (VSD)',
            'description': f'VSD ile yilda {vsd_savings_eur:.0f} EUR tasarruf potansiyeli.',
            'investment_eur': vsd_cost,
            'savings_eur_year': vsd_savings_eur,
            'payback_years': payback,
            'priority': 'high' if payback < 3 else 'medium' if payback < 5 else 'low',
        })

    # Throttle elimination
    if input_data.control_method == 'throttle' and result.throttle_loss_kW and result.throttle_loss_kW > 0.5:
        savings = result.throttle_loss_kW * input_data.operating_hours * input_data.electricity_price_eur_kwh
        recommendations.append({
            'type': 'throttle_elimination',
            'title': 'Vana Kaybi Eliminasyonu',
            'description': f'Kisma vanasi kaybi {result.throttle_loss_kW:.1f} kW. VSD ile elimine edilebilir.',
            'investment_eur': input_data.motor_power_kW * 80,
            'savings_eur_year': savings,
            'payback_years': (input_data.motor_power_kW * 80) / savings if savings > 0 else float('inf'),
            'priority': 'high',
        })

    # Impeller trim
    if result.wire_to_water_efficiency_pct and result.wire_to_water_efficiency_pct < 50:
        savings = input_data.motor_power_kW * 0.10 * input_data.operating_hours * input_data.electricity_price_eur_kwh
        recommendations.append({
            'type': 'impeller_trim',
            'title': 'Carkin Budanmasi / Degisimi',
            'description': 'Dusuk verim - cark budama veya degisimi degerlendirilebilir.',
            'investment_eur': 2000,
            'savings_eur_year': savings,
            'payback_years': 2000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # Maintenance
    if result.benchmark_comparison in ('poor', 'below_average'):
        savings = input_data.motor_power_kW * 0.05 * input_data.operating_hours * input_data.electricity_price_eur_kwh
        recommendations.append({
            'type': 'maintenance',
            'title': 'Bakim ve Kontrol',
            'description': 'Mekanik conta, yatak ve asinma kontrolu onerilir.',
            'investment_eur': 500,
            'savings_eur_year': savings,
            'payback_years': 500 / savings if savings > 0 else float('inf'),
            'priority': 'high',
        })

    # System optimization
    recommendations.append({
        'type': 'system_design',
        'title': 'Sistem Tasarimi Iyilestirme',
        'description': 'Boru caplari, dirsek sayisi ve sistem direnci optimizasyonu.',
        'investment_eur': 3000,
        'savings_eur_year': input_data.motor_power_kW * 0.03 * input_data.operating_hours * input_data.electricity_price_eur_kwh,
        'payback_years': 3000 / (input_data.motor_power_kW * 0.03 * input_data.operating_hours * input_data.electricity_price_eur_kwh) if input_data.motor_power_kW > 0 else float('inf'),
        'priority': 'low',
    })

    return recommendations


# ---------------------------------------------------------------------------
# Pump types helper
# ---------------------------------------------------------------------------

def get_pump_types() -> list:
    """Desteklenen pompa tiplerini dondurur."""
    return [
        {
            "type": "centrifugal",
            "name": "Santrifuj Pompa",
            "description": "Endustriyel santrifuj pompa analizi",
        },
        {
            "type": "positive_displacement",
            "name": "Pozitif Deplasman Pompa",
            "description": "Pozitif deplasman pompa analizi",
        },
        {
            "type": "submersible",
            "name": "Dalgic Pompa",
            "description": "Dalgic pompa analizi",
        },
        {
            "type": "vertical_turbine",
            "name": "Dikey Turbin Pompa",
            "description": "Dikey turbin pompa analizi",
        },
        {
            "type": "booster",
            "name": "Hidrofor",
            "description": "Hidrofor / booster pompa analizi",
        },
        {
            "type": "vacuum",
            "name": "Vakum Pompasi",
            "description": "Vakum pompasi analizi",
        },
    ]


# ---------------------------------------------------------------------------
# Benchmark helpers
# ---------------------------------------------------------------------------

def _get_benchmark_comparison(eta_ex: float, pump_type: str) -> str:
    """Exergy verimine gore benchmark karsilastirmasi."""
    benchmarks = {
        'centrifugal': {'poor': 35, 'average': 50, 'good': 65, 'excellent': 75},
        'positive_displacement': {'poor': 40, 'average': 55, 'good': 70, 'excellent': 80},
        'submersible': {'poor': 25, 'average': 40, 'good': 55, 'excellent': 65},
        'vertical_turbine': {'poor': 35, 'average': 50, 'good': 65, 'excellent': 75},
        'booster': {'poor': 30, 'average': 45, 'good': 60, 'excellent': 70},
        'vacuum': {'poor': 20, 'average': 35, 'good': 50, 'excellent': 60},
    }
    thresholds = benchmarks.get(pump_type, benchmarks['centrifugal'])

    if eta_ex < thresholds['poor']:
        return 'poor'
    elif eta_ex < thresholds['average']:
        return 'below_average'
    elif eta_ex < thresholds['good']:
        return 'average'
    elif eta_ex < thresholds['excellent']:
        return 'good'
    else:
        return 'excellent'


def _calculate_percentile(eta_ex: float, pump_type: str) -> int:
    """Exergy verimini 0-100 yuzdelik dilime esler."""
    benchmarks = {
        'centrifugal': {'low': 30, 'mid': 55, 'high': 75},
        'positive_displacement': {'low': 35, 'mid': 60, 'high': 80},
        'submersible': {'low': 25, 'mid': 45, 'high': 65},
        'vertical_turbine': {'low': 30, 'mid': 55, 'high': 75},
        'booster': {'low': 25, 'mid': 50, 'high': 70},
        'vacuum': {'low': 20, 'mid': 40, 'high': 60},
    }
    thresholds = benchmarks.get(pump_type, benchmarks['centrifugal'])

    if eta_ex <= thresholds['low']:
        return max(0, int(eta_ex / thresholds['low'] * 25))
    elif eta_ex <= thresholds['mid']:
        return 25 + int((eta_ex - thresholds['low']) / (thresholds['mid'] - thresholds['low']) * 25)
    elif eta_ex <= thresholds['high']:
        return 50 + int((eta_ex - thresholds['mid']) / (thresholds['high'] - thresholds['mid']) * 25)
    else:
        return min(100, 75 + int((eta_ex - thresholds['high']) / 15 * 25))


def _get_comparison_text(benchmark: str) -> str:
    """Benchmark sonucuna gore aciklama dondurur."""
    texts = {
        'poor': 'Exergy verimi dusuk. Acil iyilestirme onerilir.',
        'below_average': 'Exergy verimi ortalamanin altinda. Iyilestirme potansiyeli yuksek.',
        'average': 'Exergy verimi ortalama seviyede. Iyilestirme firsatlari mevcut.',
        'good': 'Exergy verimi iyi seviyede. Sinirli iyilestirme potansiyeli.',
        'excellent': 'Exergy verimi mukemmel. En iyi uygulama seviyesinde.',
    }
    return texts.get(benchmark, '')
