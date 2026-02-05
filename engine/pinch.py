"""
ExergyLab - Pinch Analysis Engine

Linnhoff pinch analizi motoru.
Termal akis cikarimi, sicaklik aralik tablosu, kaskat algoritma,
kompozit egri, GCC ve HEN eslestirme onerileri.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum


# ---------------------------------------------------------------------------
# Data Structures
# ---------------------------------------------------------------------------

class StreamType(str, Enum):
    HOT = "hot"
    COLD = "cold"


@dataclass
class ThermalStream:
    """Tek bir termal akis."""
    stream_id: str
    stream_type: StreamType
    equipment_name: str
    equipment_type: str
    description: str
    T_supply_C: float
    T_target_C: float
    Q_dot_kW: float
    CP_kW_per_K: float  # = Q / |delta_T|
    fluid: str = "unknown"
    phase_change: bool = False
    is_utility: bool = False

    def to_dict(self) -> dict:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type.value,
            "equipment_name": self.equipment_name,
            "equipment_type": self.equipment_type,
            "description": self.description,
            "T_supply_C": round(self.T_supply_C, 1),
            "T_target_C": round(self.T_target_C, 1),
            "Q_dot_kW": round(self.Q_dot_kW, 1),
            "CP_kW_per_K": round(self.CP_kW_per_K, 4),
            "fluid": self.fluid,
            "phase_change": self.phase_change,
            "is_utility": self.is_utility,
        }


@dataclass
class TemperatureInterval:
    """Sicaklik aralik tablosu satiri."""
    T_upper_C: float
    T_lower_C: float
    delta_T_C: float
    sum_CP_hot: float
    sum_CP_cold: float
    delta_H_kW: float
    cascade_kW: float = 0.0


@dataclass
class PinchResult:
    """Pinch analizi sonuclari."""
    is_valid: bool = True
    error_message: str = ""

    # Streams
    streams: List[dict] = field(default_factory=list)
    hot_stream_count: int = 0
    cold_stream_count: int = 0

    # Pinch point
    pinch_temperature_C: Optional[float] = None
    delta_T_min_C: float = 10.0

    # Energy targets
    QH_min_kW: float = 0.0
    QC_min_kW: float = 0.0
    max_heat_recovery_kW: float = 0.0

    # Current utility usage estimate
    QH_current_kW: float = 0.0
    QC_current_kW: float = 0.0

    # Savings
    QH_excess_kW: float = 0.0
    QC_excess_kW: float = 0.0
    savings_pct: float = 0.0
    annual_savings_kWh: float = 0.0
    annual_savings_EUR: float = 0.0

    # Composite curves (Plotly data)
    composite_curves: Optional[dict] = None

    # Grand Composite Curve (Plotly data)
    grand_composite_curve: Optional[dict] = None

    # Temperature intervals
    intervals: List[dict] = field(default_factory=list)

    # HEN matches
    hen_matches: List[dict] = field(default_factory=list)

    # Parameters
    fuel_price_eur_kwh: float = 0.08
    operating_hours: int = 8000

    def to_dict(self) -> dict:
        return {
            "is_valid": self.is_valid,
            "error_message": self.error_message,
            "streams": self.streams,
            "hot_stream_count": self.hot_stream_count,
            "cold_stream_count": self.cold_stream_count,
            "pinch_temperature_C": round(self.pinch_temperature_C, 1) if self.pinch_temperature_C is not None else None,
            "delta_T_min_C": round(self.delta_T_min_C, 1),
            "QH_min_kW": round(self.QH_min_kW, 2),
            "QC_min_kW": round(self.QC_min_kW, 2),
            "max_heat_recovery_kW": round(self.max_heat_recovery_kW, 2),
            "QH_current_kW": round(self.QH_current_kW, 2),
            "QC_current_kW": round(self.QC_current_kW, 2),
            "QH_excess_kW": round(self.QH_excess_kW, 2),
            "QC_excess_kW": round(self.QC_excess_kW, 2),
            "savings_pct": round(self.savings_pct, 1),
            "annual_savings_kWh": round(self.annual_savings_kWh, 0),
            "annual_savings_EUR": round(self.annual_savings_EUR, 0),
            "composite_curves": self.composite_curves,
            "grand_composite_curve": self.grand_composite_curve,
            "intervals": self.intervals,
            "hen_matches": self.hen_matches,
            "fuel_price_eur_kwh": self.fuel_price_eur_kwh,
            "operating_hours": self.operating_hours,
        }


# ---------------------------------------------------------------------------
# Stream extraction — 7 equipment types
# ---------------------------------------------------------------------------

_MIN_Q_KW = 5.0       # Minimum thermal power to include
_MIN_DT_C = 2.0       # Minimum temperature difference
_DEFAULT_STACK_T = 150.0  # Default stack temperature for boilers


def _safe_cp(Q_kW: float, T_supply: float, T_target: float) -> float:
    """Calculate CP = Q / |delta_T|, handle zero delta."""
    dt = abs(T_supply - T_target)
    if dt < 0.01:
        return 0.0
    return Q_kW / dt


def _make_stream(
    stream_id: str,
    stream_type: StreamType,
    equipment_name: str,
    equipment_type: str,
    description: str,
    T_supply_C: float,
    T_target_C: float,
    Q_dot_kW: float,
    fluid: str = "unknown",
) -> Optional[ThermalStream]:
    """Create a ThermalStream if it passes filters."""
    if Q_dot_kW < _MIN_Q_KW:
        return None
    if abs(T_supply_C - T_target_C) < _MIN_DT_C:
        return None
    cp = _safe_cp(Q_dot_kW, T_supply_C, T_target_C)
    if cp <= 0:
        return None
    return ThermalStream(
        stream_id=stream_id,
        stream_type=stream_type,
        equipment_name=equipment_name,
        equipment_type=equipment_type,
        description=description,
        T_supply_C=T_supply_C,
        T_target_C=T_target_C,
        Q_dot_kW=Q_dot_kW,
        CP_kW_per_K=cp,
        fluid=fluid,
    )


def _extract_boiler_streams(item, result: dict) -> List[ThermalStream]:
    """Extract hot (flue gas) and cold (feedwater) streams from boiler."""
    streams = []
    params = item.parameters

    # HOT: Flue gas waste heat
    T_flue = params.get("flue_gas_temp_C", 180)
    T_stack = _DEFAULT_STACK_T
    Q_recoverable = result.get("recoverable_heat_kW") or result.get("flue_gas_loss_kW", 0)
    if Q_recoverable and Q_recoverable > 0:
        s = _make_stream(
            stream_id=f"{item.id}_flue",
            stream_type=StreamType.HOT,
            equipment_name=item.name,
            equipment_type="boiler",
            description=f"Kazan baca gazi ({T_flue}°C → {T_stack}°C)",
            T_supply_C=T_flue,
            T_target_C=T_stack,
            Q_dot_kW=Q_recoverable,
            fluid="flue_gas",
        )
        if s:
            streams.append(s)

    # COLD: Feedwater preheat demand
    T_feedwater = params.get("feedwater_temp_C", 80)
    T_steam = params.get("steam_temp_C") or params.get("steam_pressure_bar", 10) * 8 + 100
    # Useful heat = exergy_in * thermal_efficiency
    thermal_eff = result.get("thermal_efficiency_pct", 80) / 100.0
    Q_useful = result.get("exergy_in_kW", 0) * thermal_eff
    if Q_useful > 0 and T_steam > T_feedwater:
        s = _make_stream(
            stream_id=f"{item.id}_feedwater",
            stream_type=StreamType.COLD,
            equipment_name=item.name,
            equipment_type="boiler",
            description=f"Kazan besleme suyu ({T_feedwater}°C → {T_steam}°C)",
            T_supply_C=T_feedwater,
            T_target_C=T_steam,
            Q_dot_kW=Q_useful,
            fluid="water",
        )
        if s:
            streams.append(s)

    return streams


def _extract_compressor_streams(item, result: dict) -> List[ThermalStream]:
    """Extract hot stream (compression heat) from compressor."""
    streams = []
    params = item.parameters

    T_outlet = params.get("outlet_temp_C", 80)
    T_inlet = params.get("inlet_temp_C") or params.get("ambient_temp_C", 25)
    T_aftercooler = T_inlet + 15  # Aftercooler target

    Q_heat = result.get("recoverable_heat_kW", 0)
    if not Q_heat or Q_heat <= 0:
        Q_heat = result.get("exergy_destroyed_kW", 0) * 0.7

    if Q_heat > 0 and T_outlet > T_aftercooler:
        s = _make_stream(
            stream_id=f"{item.id}_comp_heat",
            stream_type=StreamType.HOT,
            equipment_name=item.name,
            equipment_type="compressor",
            description=f"Kompresor atik isisi ({T_outlet}°C → {T_aftercooler}°C)",
            T_supply_C=T_outlet,
            T_target_C=T_aftercooler,
            Q_dot_kW=Q_heat,
            fluid="compressed_air",
        )
        if s:
            streams.append(s)

    return streams


def _extract_chiller_streams(item, result: dict) -> List[ThermalStream]:
    """Extract hot (condenser) and cold (evaporator) streams from chiller."""
    streams = []
    params = item.parameters

    # HOT: Condenser rejection
    T_cw_return = params.get("cw_return_temp_C", 35)
    T_cw_supply = params.get("cw_supply_temp_C", 30)
    Q_evap = params.get("cooling_capacity_kW", 0)
    W_comp = params.get("compressor_power_kW", 0)
    Q_cond = Q_evap + W_comp if Q_evap else result.get("exergy_in_kW", 0) * 1.2

    if Q_cond > 0 and T_cw_return > T_cw_supply:
        s = _make_stream(
            stream_id=f"{item.id}_condenser",
            stream_type=StreamType.HOT,
            equipment_name=item.name,
            equipment_type="chiller",
            description=f"Chiller kondenser ({T_cw_return}°C → {T_cw_supply}°C)",
            T_supply_C=T_cw_return,
            T_target_C=T_cw_supply,
            Q_dot_kW=Q_cond,
            fluid="water",
        )
        if s:
            streams.append(s)

    # COLD: Evaporator cooling demand
    T_chw_return = params.get("chw_return_temp_C", 12)
    T_chw_supply = params.get("chw_supply_temp_C", 7)
    if Q_evap > 0 and T_chw_return > T_chw_supply:
        s = _make_stream(
            stream_id=f"{item.id}_evaporator",
            stream_type=StreamType.COLD,
            equipment_name=item.name,
            equipment_type="chiller",
            description=f"Chiller evaporator ({T_chw_supply}°C → {T_chw_return}°C)",
            T_supply_C=T_chw_supply,
            T_target_C=T_chw_return,
            Q_dot_kW=Q_evap,
            fluid="chilled_water",
        )
        if s:
            streams.append(s)

    return streams


def _extract_pump_streams(item, result: dict) -> List[ThermalStream]:
    """Pumps are thermally insignificant — return empty."""
    return []


def _extract_heat_exchanger_streams(item, result: dict) -> List[ThermalStream]:
    """Extract hot and cold streams from heat exchanger."""
    streams = []
    params = item.parameters

    T_hot_in = params.get("hot_inlet_temp_C", 90)
    T_hot_out = params.get("hot_outlet_temp_C", 70)
    T_cold_in = params.get("cold_inlet_temp_C", 20)
    T_cold_out = params.get("cold_outlet_temp_C", 50)
    Q = result.get("heat_duty_kW") or params.get("heat_duty_kW", 0)

    if Q > 0:
        # HOT side
        if T_hot_in > T_hot_out:
            s = _make_stream(
                stream_id=f"{item.id}_hot",
                stream_type=StreamType.HOT,
                equipment_name=item.name,
                equipment_type="heat_exchanger",
                description=f"HX sicak akis ({T_hot_in}°C → {T_hot_out}°C)",
                T_supply_C=T_hot_in,
                T_target_C=T_hot_out,
                Q_dot_kW=Q,
                fluid=params.get("hot_fluid", "water"),
            )
            if s:
                streams.append(s)

        # COLD side
        if T_cold_out > T_cold_in:
            s = _make_stream(
                stream_id=f"{item.id}_cold",
                stream_type=StreamType.COLD,
                equipment_name=item.name,
                equipment_type="heat_exchanger",
                description=f"HX soguk akis ({T_cold_in}°C → {T_cold_out}°C)",
                T_supply_C=T_cold_in,
                T_target_C=T_cold_out,
                Q_dot_kW=Q,
                fluid=params.get("cold_fluid", "water"),
            )
            if s:
                streams.append(s)

    return streams


def _extract_steam_turbine_streams(item, result: dict) -> List[ThermalStream]:
    """Extract hot stream (exhaust heat) from steam turbine."""
    streams = []
    params = item.parameters

    turbine_type = params.get("turbine_type", "backpressure")
    T_exhaust = params.get("outlet_temp_C") or 150
    T_ambient = params.get("ambient_temp_C", 25)
    T_target = T_ambient + 20  # Cooling to near ambient

    Q_exhaust = result.get("recoverable_heat_kW", 0)
    if not Q_exhaust or Q_exhaust <= 0:
        Q_exhaust = result.get("exhaust_exergy_kW", 0) * 1.5  # Approximate thermal from exergy

    if Q_exhaust > 0 and T_exhaust > T_target:
        s = _make_stream(
            stream_id=f"{item.id}_exhaust",
            stream_type=StreamType.HOT,
            equipment_name=item.name,
            equipment_type="steam_turbine",
            description=f"Turbin egzoz ({T_exhaust}°C → {T_target}°C)",
            T_supply_C=T_exhaust,
            T_target_C=T_target,
            Q_dot_kW=Q_exhaust,
            fluid="steam",
        )
        if s:
            streams.append(s)

    return streams


def _extract_dryer_streams(item, result: dict) -> List[ThermalStream]:
    """Extract hot (exhaust) and cold (drying load) streams from dryer."""
    streams = []
    params = item.parameters

    # HOT: Exhaust air
    T_air_out = params.get("air_outlet_temp_C", 80)
    T_ambient = params.get("ambient_temp_C", 25)
    Q_recoverable = result.get("recoverable_heat_kW", 0)
    if not Q_recoverable or Q_recoverable <= 0:
        Q_recoverable = result.get("exhaust_exergy_kW", 0) * 1.5

    if Q_recoverable > 0 and T_air_out > T_ambient:
        s = _make_stream(
            stream_id=f"{item.id}_exhaust",
            stream_type=StreamType.HOT,
            equipment_name=item.name,
            equipment_type="dryer",
            description=f"Kurutucu egzoz ({T_air_out}°C → {T_ambient}°C)",
            T_supply_C=T_air_out,
            T_target_C=T_ambient,
            Q_dot_kW=Q_recoverable,
            fluid="moist_air",
        )
        if s:
            streams.append(s)

    # COLD: Drying load (supply air heating)
    T_product_in = params.get("product_inlet_temp_C", 25)
    T_supply = params.get("supply_temp_C", 200)
    Q_input = result.get("heat_input_kW") or params.get("heat_input_kW", 0)

    if Q_input > 0 and T_supply > T_product_in:
        s = _make_stream(
            stream_id=f"{item.id}_drying",
            stream_type=StreamType.COLD,
            equipment_name=item.name,
            equipment_type="dryer",
            description=f"Kurutucu besleme ({T_product_in}°C → {T_supply}°C)",
            T_supply_C=T_product_in,
            T_target_C=T_supply,
            Q_dot_kW=Q_input,
            fluid="air",
        )
        if s:
            streams.append(s)

    return streams


# Dispatcher map
_EXTRACTORS = {
    "boiler": _extract_boiler_streams,
    "compressor": _extract_compressor_streams,
    "chiller": _extract_chiller_streams,
    "pump": _extract_pump_streams,
    "heat_exchanger": _extract_heat_exchanger_streams,
    "steam_turbine": _extract_steam_turbine_streams,
    "dryer": _extract_dryer_streams,
}


def extract_thermal_streams(
    equipment_list,
    analysis_results: Dict[str, dict],
    include_pumps: bool = False,
) -> List[ThermalStream]:
    """
    Extract thermal streams from all equipment for pinch analysis.

    Args:
        equipment_list: List of EquipmentItem objects
        analysis_results: Dict mapping equipment id to analysis result dict
        include_pumps: Whether to include pump streams (default False)

    Returns:
        List of ThermalStream objects
    """
    streams = []
    for item in equipment_list:
        eq_type = item.equipment_type
        if eq_type == "pump" and not include_pumps:
            continue

        result = analysis_results.get(item.id)
        if not result:
            continue

        extractor = _EXTRACTORS.get(eq_type)
        if not extractor:
            continue

        extracted = extractor(item, result)
        streams.extend(extracted)

    return streams


# ---------------------------------------------------------------------------
# Pinch Calculation Core
# ---------------------------------------------------------------------------

def compute_shifted_temperatures(
    streams: List[ThermalStream],
    delta_T_min_C: float,
) -> List[float]:
    """
    Compute shifted temperatures for all streams.

    Hot streams: T_shifted = T - delta_T_min/2
    Cold streams: T_shifted = T + delta_T_min/2

    Returns sorted unique list (descending).
    """
    half_dt = delta_T_min_C / 2.0
    temps = set()

    for s in streams:
        if s.stream_type == StreamType.HOT:
            temps.add(s.T_supply_C - half_dt)
            temps.add(s.T_target_C - half_dt)
        else:
            temps.add(s.T_supply_C + half_dt)
            temps.add(s.T_target_C + half_dt)

    return sorted(temps, reverse=True)


def create_temperature_intervals(
    streams: List[ThermalStream],
    shifted_temps: List[float],
    delta_T_min_C: float,
) -> List[TemperatureInterval]:
    """
    Create temperature interval table.

    For each adjacent pair of shifted temps, find active streams
    and compute heat balance.
    """
    half_dt = delta_T_min_C / 2.0
    intervals = []

    for i in range(len(shifted_temps) - 1):
        T_upper = shifted_temps[i]
        T_lower = shifted_temps[i + 1]
        delta_T = T_upper - T_lower

        if delta_T < 0.001:
            continue

        # Find active hot streams in this interval
        # Hot stream shifted: [T_target - dt/2, T_supply - dt/2]
        sum_CP_hot = 0.0
        for s in streams:
            if s.stream_type == StreamType.HOT:
                s_upper = s.T_supply_C - half_dt
                s_lower = s.T_target_C - half_dt
                if s_upper >= T_upper - 0.001 and s_lower <= T_lower + 0.001:
                    sum_CP_hot += s.CP_kW_per_K

        # Find active cold streams in this interval
        # Cold stream shifted: [T_supply + dt/2, T_target + dt/2]
        sum_CP_cold = 0.0
        for s in streams:
            if s.stream_type == StreamType.COLD:
                s_lower = s.T_supply_C + half_dt
                s_upper = s.T_target_C + half_dt
                if s_upper >= T_upper - 0.001 and s_lower <= T_lower + 0.001:
                    sum_CP_cold += s.CP_kW_per_K

        delta_H = (sum_CP_hot - sum_CP_cold) * delta_T

        intervals.append(TemperatureInterval(
            T_upper_C=T_upper,
            T_lower_C=T_lower,
            delta_T_C=delta_T,
            sum_CP_hot=sum_CP_hot,
            sum_CP_cold=sum_CP_cold,
            delta_H_kW=delta_H,
        ))

    return intervals


def solve_cascade(
    intervals: List[TemperatureInterval],
) -> Tuple[float, float, Optional[float], List[float]]:
    """
    Solve the heat cascade (Problem Table Algorithm).

    Returns:
        (QH_min, QC_min, pinch_shifted_T, cascade_values)

    QH_min: minimum hot utility
    QC_min: minimum cold utility
    pinch_shifted_T: shifted temperature at pinch point (cascade = 0)
    cascade_values: cascade heat flow at each temperature level
    """
    if not intervals:
        return 0.0, 0.0, None, []

    # First pass: cascade with QH = 0
    cascade = [0.0]
    for interval in intervals:
        cascade.append(cascade[-1] + interval.delta_H_kW)

    # QH_min = |min(cascade)| if any negative
    min_cascade = min(cascade)
    QH_min = abs(min_cascade) if min_cascade < 0 else 0.0

    # Second pass: corrected cascade
    corrected = [c + QH_min for c in cascade]

    # QC_min = last value
    QC_min = corrected[-1] if corrected else 0.0

    # Pinch = where corrected cascade ≈ 0
    pinch_T = None
    for i, val in enumerate(corrected):
        if abs(val) < 0.01:
            if i == 0:
                pinch_T = intervals[0].T_upper_C if intervals else None
            elif i <= len(intervals):
                pinch_T = intervals[i - 1].T_lower_C
            break

    # Store cascade values on intervals
    for i, interval in enumerate(intervals):
        interval.cascade_kW = corrected[i + 1]

    return QH_min, QC_min, pinch_T, corrected


def generate_composite_curves(
    streams: List[ThermalStream],
    QH_min_kW: float,
) -> dict:
    """
    Generate hot and cold composite curves for Plotly visualization.

    Returns dict with hot_curve, cold_curve, pinch_point data.
    """
    hot_streams = [s for s in streams if s.stream_type == StreamType.HOT]
    cold_streams = [s for s in streams if s.stream_type == StreamType.COLD]

    hot_curve = _build_composite(hot_streams, descending=True)
    cold_curve = _build_composite(cold_streams, descending=False)

    # Shift cold curve by QH_min for pinch contact
    cold_curve_shifted = [(T, H + QH_min_kW) for T, H in cold_curve]

    return {
        "hot_curve": {
            "H_kW": [round(h, 2) for _, h in hot_curve],
            "T_C": [round(t, 1) for t, _ in hot_curve],
        },
        "cold_curve": {
            "H_kW": [round(h, 2) for _, h in cold_curve_shifted],
            "T_C": [round(t, 1) for t, _ in cold_curve_shifted],
        },
        "QH_min_kW": round(QH_min_kW, 2),
    }


def _build_composite(
    streams: List[ThermalStream],
    descending: bool = True,
) -> List[Tuple[float, float]]:
    """
    Build a composite curve from a list of streams.

    Returns list of (T, cumulative_H) points.
    """
    if not streams:
        return []

    # Collect all temperature breakpoints
    temps = set()
    for s in streams:
        temps.add(s.T_supply_C)
        temps.add(s.T_target_C)
    temps = sorted(temps, reverse=descending)

    if len(temps) < 2:
        return [(temps[0], 0.0)]

    # Build cumulative enthalpy
    points = [(temps[0], 0.0)]
    cumH = 0.0

    for i in range(len(temps) - 1):
        T_high = max(temps[i], temps[i + 1])
        T_low = min(temps[i], temps[i + 1])
        dT = T_high - T_low

        # Sum CP of active streams in this interval
        total_CP = 0.0
        for s in streams:
            s_high = max(s.T_supply_C, s.T_target_C)
            s_low = min(s.T_supply_C, s.T_target_C)
            if s_high >= T_high - 0.001 and s_low <= T_low + 0.001:
                total_CP += s.CP_kW_per_K

        cumH += total_CP * dT
        points.append((temps[i + 1], cumH))

    return points


def generate_grand_composite_curve(
    intervals: List[TemperatureInterval],
    cascade: List[float],
) -> dict:
    """
    Generate Grand Composite Curve (GCC) data.

    GCC: shifted temperature vs net heat flow (cascade values).
    """
    if not intervals or not cascade:
        return {"H_kW": [], "T_shifted_C": [], "pinch_T_C": None}

    T_shifted = [intervals[0].T_upper_C]
    H_kW = [cascade[0]]

    for i, interval in enumerate(intervals):
        T_shifted.append(interval.T_lower_C)
        H_kW.append(cascade[i + 1])

    # Find pinch (where H ≈ 0)
    pinch_T = None
    for i, h in enumerate(H_kW):
        if abs(h) < 0.01:
            pinch_T = T_shifted[i]
            break

    return {
        "H_kW": [round(h, 2) for h in H_kW],
        "T_shifted_C": [round(t, 1) for t in T_shifted],
        "pinch_T_C": round(pinch_T, 1) if pinch_T is not None else None,
    }


# ---------------------------------------------------------------------------
# HEN (Heat Exchanger Network) Matching
# ---------------------------------------------------------------------------

def suggest_hen_matches(
    streams: List[ThermalStream],
    pinch_T_shifted: Optional[float],
    delta_T_min_C: float,
) -> List[dict]:
    """
    Suggest heat exchanger network matches.

    Split streams by pinch into above/below regions.
    Greedy matching: largest Q first.
    """
    if pinch_T_shifted is None:
        # No pinch — match all together
        return _match_streams(streams, delta_T_min_C, "full")

    half_dt = delta_T_min_C / 2.0
    matches = []

    # Split streams by pinch
    above_hot = []
    above_cold = []
    below_hot = []
    below_cold = []

    for s in streams:
        if s.stream_type == StreamType.HOT:
            s_shifted_upper = s.T_supply_C - half_dt
            s_shifted_lower = s.T_target_C - half_dt
            if s_shifted_upper > pinch_T_shifted + 0.001:
                above_hot.append(s)
            if s_shifted_lower < pinch_T_shifted - 0.001:
                below_hot.append(s)
        else:
            s_shifted_upper = s.T_target_C + half_dt
            s_shifted_lower = s.T_supply_C + half_dt
            if s_shifted_upper > pinch_T_shifted + 0.001:
                above_cold.append(s)
            if s_shifted_lower < pinch_T_shifted - 0.001:
                below_cold.append(s)

    # Match above pinch
    above_streams = above_hot + above_cold
    matches.extend(_match_streams(above_streams, delta_T_min_C, "above_pinch"))

    # Match below pinch
    below_streams = below_hot + below_cold
    matches.extend(_match_streams(below_streams, delta_T_min_C, "below_pinch"))

    return matches


def _match_streams(
    streams: List[ThermalStream],
    delta_T_min_C: float,
    region: str,
) -> List[dict]:
    """Greedy matching of hot and cold streams."""
    hot = sorted(
        [s for s in streams if s.stream_type == StreamType.HOT],
        key=lambda s: s.Q_dot_kW, reverse=True,
    )
    cold = sorted(
        [s for s in streams if s.stream_type == StreamType.COLD],
        key=lambda s: s.Q_dot_kW, reverse=True,
    )

    matches = []
    hot_remaining = {s.stream_id: s.Q_dot_kW for s in hot}
    cold_remaining = {s.stream_id: s.Q_dot_kW for s in cold}

    for h in hot:
        for c in cold:
            if hot_remaining.get(h.stream_id, 0) <= 0:
                break
            if cold_remaining.get(c.stream_id, 0) <= 0:
                continue

            # Check temperature feasibility
            T_h_supply = max(h.T_supply_C, h.T_target_C)
            T_c_target = max(c.T_supply_C, c.T_target_C)
            if T_h_supply - T_c_target < delta_T_min_C:
                continue

            Q_exchange = min(hot_remaining[h.stream_id], cold_remaining[c.stream_id])
            if Q_exchange < _MIN_Q_KW:
                continue

            hot_remaining[h.stream_id] -= Q_exchange
            cold_remaining[c.stream_id] -= Q_exchange

            matches.append({
                "hot_stream": h.stream_id,
                "hot_equipment": h.equipment_name,
                "cold_stream": c.stream_id,
                "cold_equipment": c.equipment_name,
                "Q_exchange_kW": round(Q_exchange, 2),
                "T_hot_supply_C": round(h.T_supply_C, 1),
                "T_cold_target_C": round(c.T_target_C, 1),
                "region": region,
                "description": (
                    f"{h.equipment_name} ({h.T_supply_C:.0f}°C) → "
                    f"{c.equipment_name} ({c.T_target_C:.0f}°C): "
                    f"{Q_exchange:.1f} kW"
                ),
            })

    return matches


# ---------------------------------------------------------------------------
# Feasibility & Utility Estimation
# ---------------------------------------------------------------------------

def check_pinch_feasibility(
    streams: List[ThermalStream],
    delta_T_min_C: float = 10.0,
) -> Tuple[bool, str]:
    """
    Check if pinch analysis is feasible.

    Requires: >= 1 hot stream, >= 1 cold stream, total Q > 50 kW,
    and temperature overlap between hot and cold ranges.
    """
    hot = [s for s in streams if s.stream_type == StreamType.HOT]
    cold = [s for s in streams if s.stream_type == StreamType.COLD]

    if not hot:
        return False, "Sicak akis bulunamadi"
    if not cold:
        return False, "Soguk akis bulunamadi"

    total_Q = sum(s.Q_dot_kW for s in streams)
    if total_Q < 50:
        return False, f"Toplam termal yuk cok dusuk ({total_Q:.1f} kW < 50 kW)"

    # Check temperature overlap
    hot_max = max(max(s.T_supply_C, s.T_target_C) for s in hot)
    hot_min = min(min(s.T_supply_C, s.T_target_C) for s in hot)
    cold_max = max(max(s.T_supply_C, s.T_target_C) for s in cold)
    cold_min = min(min(s.T_supply_C, s.T_target_C) for s in cold)

    if hot_min > cold_max:
        return False, "Sicak ve soguk akislar arasinda sicaklik ortusme yok"

    return True, ""


def estimate_current_utility_usage(
    streams: List[ThermalStream],
    equipment_list,
) -> Tuple[float, float]:
    """
    Estimate current hot (QH) and cold (QC) utility usage.

    Hot utility ≈ sum of boiler/dryer heat inputs
    Cold utility ≈ sum of chiller/condenser rejections
    """
    QH_current = 0.0
    QC_current = 0.0

    for s in streams:
        if s.stream_type == StreamType.COLD:
            # Cold streams need heating → contributes to hot utility demand
            QH_current += s.Q_dot_kW
        else:
            # Hot streams need cooling → contributes to cold utility demand
            QC_current += s.Q_dot_kW

    return QH_current, QC_current


def calculate_savings(
    QH_min_kW: float,
    QC_min_kW: float,
    QH_current_kW: float,
    QC_current_kW: float,
    fuel_price_eur_kwh: float,
    operating_hours: int,
) -> dict:
    """Calculate energy and cost savings from pinch analysis."""
    QH_excess = max(0, QH_current_kW - QH_min_kW)
    QC_excess = max(0, QC_current_kW - QC_min_kW)

    savings_pct = (QH_excess / QH_current_kW * 100) if QH_current_kW > 0 else 0.0

    annual_savings_kWh = QH_excess * operating_hours
    annual_savings_EUR = annual_savings_kWh * fuel_price_eur_kwh

    return {
        "QH_excess_kW": QH_excess,
        "QC_excess_kW": QC_excess,
        "savings_pct": savings_pct,
        "annual_savings_kWh": annual_savings_kWh,
        "annual_savings_EUR": annual_savings_EUR,
    }


# ---------------------------------------------------------------------------
# Main Orchestrator
# ---------------------------------------------------------------------------

def analyze_pinch(
    equipment_list,
    analysis_results: Dict[str, dict],
    delta_T_min_C: float = 10.0,
    fuel_price_eur_kwh: float = 0.08,
    operating_hours: int = 8000,
    include_pumps: bool = False,
) -> PinchResult:
    """
    Main pinch analysis orchestrator.

    Args:
        equipment_list: List of EquipmentItem objects
        analysis_results: Dict mapping equipment id to result dict
        delta_T_min_C: Minimum temperature approach [°C]
        fuel_price_eur_kwh: Fuel price for savings calculation
        operating_hours: Annual operating hours
        include_pumps: Whether to include pump streams

    Returns:
        PinchResult with all analysis data
    """
    # 1. Extract streams
    streams = extract_thermal_streams(
        equipment_list, analysis_results, include_pumps=include_pumps
    )

    hot_streams = [s for s in streams if s.stream_type == StreamType.HOT]
    cold_streams = [s for s in streams if s.stream_type == StreamType.COLD]

    # 2. Check feasibility
    feasible, reason = check_pinch_feasibility(streams, delta_T_min_C)
    if not feasible:
        return PinchResult(
            is_valid=False,
            error_message=reason,
            streams=[s.to_dict() for s in streams],
            hot_stream_count=len(hot_streams),
            cold_stream_count=len(cold_streams),
            delta_T_min_C=delta_T_min_C,
            fuel_price_eur_kwh=fuel_price_eur_kwh,
            operating_hours=operating_hours,
        )

    # 3. Compute shifted temperatures
    shifted_temps = compute_shifted_temperatures(streams, delta_T_min_C)

    # 4. Create temperature intervals
    intervals = create_temperature_intervals(streams, shifted_temps, delta_T_min_C)

    # 5. Solve cascade
    QH_min, QC_min, pinch_T_shifted, cascade = solve_cascade(intervals)

    # Compute actual pinch temperature from shifted
    pinch_temp_actual = None
    if pinch_T_shifted is not None:
        pinch_temp_actual = pinch_T_shifted + delta_T_min_C / 2.0

    # Max heat recovery
    total_Q_hot = sum(s.Q_dot_kW for s in hot_streams)
    total_Q_cold = sum(s.Q_dot_kW for s in cold_streams)
    max_recovery = min(total_Q_hot, total_Q_cold) - QH_min if QH_min > 0 else min(total_Q_hot, total_Q_cold)
    max_recovery = max(0, total_Q_hot - QC_min) if total_Q_hot > 0 else 0

    # 6. Generate composite curves
    composite = generate_composite_curves(streams, QH_min)

    # 7. Generate GCC
    gcc = generate_grand_composite_curve(intervals, cascade)

    # 8. Estimate current utility
    QH_current, QC_current = estimate_current_utility_usage(streams, equipment_list)

    # 9. HEN matches
    hen_matches = suggest_hen_matches(streams, pinch_T_shifted, delta_T_min_C)

    # 10. Calculate savings
    savings = calculate_savings(
        QH_min, QC_min, QH_current, QC_current,
        fuel_price_eur_kwh, operating_hours,
    )

    # Max recovery = total_Q_hot + total_Q_cold - QH_min - QC_min (heat balance)
    max_recovery = (total_Q_hot + total_Q_cold - QH_min - QC_min) / 2.0

    # 11. Assemble result
    return PinchResult(
        is_valid=True,
        streams=[s.to_dict() for s in streams],
        hot_stream_count=len(hot_streams),
        cold_stream_count=len(cold_streams),
        pinch_temperature_C=pinch_temp_actual,
        delta_T_min_C=delta_T_min_C,
        QH_min_kW=QH_min,
        QC_min_kW=QC_min,
        max_heat_recovery_kW=max(max_recovery, 0),
        QH_current_kW=QH_current,
        QC_current_kW=QC_current,
        QH_excess_kW=savings["QH_excess_kW"],
        QC_excess_kW=savings["QC_excess_kW"],
        savings_pct=savings["savings_pct"],
        annual_savings_kWh=savings["annual_savings_kWh"],
        annual_savings_EUR=savings["annual_savings_EUR"],
        composite_curves=composite,
        grand_composite_curve=gcc,
        intervals=[
            {
                "T_upper_C": round(iv.T_upper_C, 1),
                "T_lower_C": round(iv.T_lower_C, 1),
                "delta_T_C": round(iv.delta_T_C, 1),
                "sum_CP_hot": round(iv.sum_CP_hot, 4),
                "sum_CP_cold": round(iv.sum_CP_cold, 4),
                "delta_H_kW": round(iv.delta_H_kW, 2),
                "cascade_kW": round(iv.cascade_kW, 2),
            }
            for iv in intervals
        ],
        hen_matches=hen_matches,
        fuel_price_eur_kwh=fuel_price_eur_kwh,
        operating_hours=operating_hours,
    )
