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

    # AV/UN split for destruction node
    av_kW = getattr(result, 'exergy_destroyed_avoidable_kW', 0.0) or 0.0
    un_kW = getattr(result, 'exergy_destroyed_unavoidable_kW', 0.0) or 0.0
    has_av_un = (av_kW > 0 or un_kW > 0)

    if has_av_un:
        # Scale AV/UN to match normalized irreversibility
        av_un_total = av_kW + un_kW
        if av_un_total > 0:
            av_norm = pure_irreversibility_norm * (av_kW / av_un_total)
            un_norm = pure_irreversibility_norm * (un_kW / av_un_total)
        else:
            av_norm = pure_irreversibility_norm
            un_norm = 0.0

        nodes = [
            {"id": 0, "name": "Elektrik Enerjisi", "name_en": "Electrical Energy"},
            {"id": 1, "name": "Kompresör", "name_en": "Compressor"},
            {"id": 2, "name": "Basınçlı Hava", "name_en": "Compressed Air"},
            {"id": 3, "name": "Isı (Geri Kazanılabilir)", "name_en": "Heat (Recoverable)"},
            {"id": 4, "name": "Exergy Yıkımı (Önlenebilir)", "name_en": "Exergy Destruction (Avoidable)", "color": "#e74c3c"},
            {"id": 5, "name": "Exergy Yıkımı (Önlenemez)", "name_en": "Exergy Destruction (Unavoidable)", "color": "#95a5a6"},
        ]

        links = [
            {"source": 0, "target": 1, "value": round(Ex_in, 2), "label": "Elektrik Girişi"},
            {"source": 1, "target": 2, "value": round(Ex_out_norm, 2), "label": "Basınçlı Hava Exergy"},
            {"source": 1, "target": 3, "value": round(recoverable_heat_norm, 2), "label": "Geri Kazanılabilir Isı"},
        ]
        if av_norm > 0.01:
            links.append({"source": 1, "target": 4, "value": round(av_norm, 2), "label": "Önlenebilir Kayıplar"})
        if un_norm > 0.01:
            links.append({"source": 1, "target": 5, "value": round(un_norm, 2), "label": "Önlenemez Kayıplar"})
    else:
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
            "exergy_destroyed_avoidable_kW": round(av_kW, 2),
            "exergy_destroyed_unavoidable_kW": round(un_kW, 2),
            "avoidable_ratio_pct": round(getattr(result, 'avoidable_ratio_pct', 0.0) or 0.0, 1),
        },
    }
