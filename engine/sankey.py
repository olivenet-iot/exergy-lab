"""
ExergyLab - Sankey Diagram Data Generator

Ekipman exergy akis diyagrami verisi olusturur.
"""

from .compressor import CompressorResult
from .boiler import BoilerResult, generate_boiler_sankey_data
from .chiller import ChillerResult, generate_chiller_sankey_data
from .pump import PumpResult, generate_pump_sankey_data
from .heat_exchanger import HeatExchangerResult, generate_heat_exchanger_sankey_data
from .steam_turbine import SteamTurbineResult, generate_steam_turbine_sankey_data
from .dryer import DryerResult, generate_dryer_sankey_data
from .core import DeadState, heat_exergy


def generate_sankey_data(result, equipment_subtype: str = "screw") -> dict:
    """
    Sankey diyagrami icin node ve link verisi olusturur.

    Result tipine gore uygun sankey fonksiyonuna dispatch yapar.

    Args:
        result: Analiz sonucu (CompressorResult, BoilerResult, ChillerResult, PumpResult)
        equipment_subtype: Ekipman alt tipi

    Returns:
        dict: {nodes: [...], links: [...], summary: {...}}
    """
    if isinstance(result, BoilerResult):
        return generate_boiler_sankey_data(result, equipment_subtype)
    elif isinstance(result, ChillerResult):
        return generate_chiller_sankey_data(result, equipment_subtype)
    elif isinstance(result, PumpResult):
        return generate_pump_sankey_data(result, equipment_subtype)
    elif isinstance(result, HeatExchangerResult):
        return generate_heat_exchanger_sankey_data(result, equipment_subtype)
    elif isinstance(result, SteamTurbineResult):
        return generate_steam_turbine_sankey_data(result, equipment_subtype)
    elif isinstance(result, DryerResult):
        return generate_dryer_sankey_data(result, equipment_subtype)
    else:
        # Default: compressor sankey (original code)
        return _generate_compressor_sankey_data(result, equipment_subtype)


def _generate_compressor_sankey_data(result: CompressorResult, compressor_type: str = "screw") -> dict:
    """
    Kompresor Sankey diyagrami icin node ve link verisi olusturur.

    Exergy destroyed, geri kazanilabilir isi ve saf tersinmezlik olarak ayrilir.
    Enerji dengesi saglanir (giris = cikislar toplami).
    """
    Ex_in = result.exergy_in_kW
    Ex_out = result.exergy_out_kW
    Ex_destroyed = result.exergy_destroyed_kW

    # Geri kazanilabilir isi exergy'si
    recoverable_heat = result.recoverable_heat_kW or 0.0

    # Saf tersinmezlik
    pure_irreversibility = max(0.0, Ex_destroyed - recoverable_heat)

    # Normalizasyon
    total_out = Ex_out + recoverable_heat + pure_irreversibility
    if total_out > 0 and abs(total_out - Ex_in) > 0.01:
        scale = Ex_in / total_out
        Ex_out_norm = Ex_out * scale
        recoverable_heat_norm = recoverable_heat * scale
        pure_irreversibility_norm = pure_irreversibility * scale
    else:
        Ex_out_norm = Ex_out
        recoverable_heat_norm = recoverable_heat
        pure_irreversibility_norm = pure_irreversibility

    nodes = [
        {"id": 0, "name": "Elektrik Enerjisi", "name_en": "Electrical Energy"},
        {"id": 1, "name": "Kompresör", "name_en": "Compressor"},
        {"id": 2, "name": "Basınçlı Hava", "name_en": "Compressed Air"},
        {"id": 3, "name": "Isı (Geri Kazanılabilir)", "name_en": "Heat (Recoverable)"},
        {"id": 4, "name": "Exergy Yıkımı", "name_en": "Exergy Destruction"},
    ]

    links = [
        {
            "source": 0,
            "target": 1,
            "value": round(Ex_in, 2),
            "label": "Elektrik Girişi",
        },
        {
            "source": 1,
            "target": 2,
            "value": round(Ex_out_norm, 2),
            "label": "Basınçlı Hava Exergy",
        },
        {
            "source": 1,
            "target": 3,
            "value": round(recoverable_heat_norm, 2),
            "label": "Geri Kazanılabilir Isı",
        },
        {
            "source": 1,
            "target": 4,
            "value": round(pure_irreversibility_norm, 2),
            "label": "Tersinmezlik Kayıpları",
        },
    ]

    return {
        "nodes": nodes,
        "links": links,
        "summary": {
            "total_input_kW": round(Ex_in, 2),
            "useful_output_kW": round(Ex_out_norm, 2),
            "recoverable_heat_kW": round(recoverable_heat_norm, 2),
            "irreversibility_kW": round(pure_irreversibility_norm, 2),
            "efficiency_pct": round(result.exergy_efficiency_pct, 1),
        },
    }
