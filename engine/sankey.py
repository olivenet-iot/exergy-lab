"""
ExergyLab - Sankey Diagram Data Generator

Kompresör exergy akış diyagramı verisi oluşturur.
"""

from .compressor import CompressorResult
from .core import DeadState, heat_exergy


def generate_sankey_data(result: CompressorResult, compressor_type: str = "screw") -> dict:
    """
    Sankey diyagramı için node ve link verisi oluşturur.

    Exergy destroyed, geri kazanılabilir ısı ve saf tersinmezlik olarak ayrılır.
    Enerji dengesi sağlanır (giriş = çıkışlar toplamı).

    Args:
        result: Kompresör analiz sonucu
        compressor_type: Kompresör tipi

    Returns:
        dict: {nodes: [...], links: [...]}
    """
    Ex_in = result.exergy_in_kW
    Ex_out = result.exergy_out_kW
    Ex_destroyed = result.exergy_destroyed_kW

    # Geri kazanılabilir ısı exergy'si (atık ısının exergy değeri)
    recoverable_heat = result.recoverable_heat_kW or 0.0

    # Saf tersinmezlik = toplam yıkım - geri kazanılabilir ısı exergy
    pure_irreversibility = max(0.0, Ex_destroyed - recoverable_heat)

    # Normalizasyon: çıkışlar toplamı girişe eşit olmalı
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
