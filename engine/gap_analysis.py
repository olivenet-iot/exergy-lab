"""
Exergetic Gap Analysis — Top-down proses analizi.

Proses tanımı + ekipman analiz sonuçlarını birleştirerek
3 katmanlı exergetic gap analizi yapar:

1. Termodinamik Minimum (ideal, tersinir proses)
2. BAT (Best Available Technology) referansı
3. Mevcut Tesis (actual) — factory aggregates'ten

Referans: Tsatsaronis & Moung-Ho Park, "On Avoidable and Unavoidable
Exergy Destructions", Energy, 2002
"""

import dataclasses
from dataclasses import dataclass, field


@dataclass
class GapAnalysisResult:
    """Top-down gap analizi sonucu."""

    # Proses bilgisi
    process_type: str
    process_label: str
    subcategory: str

    # 3 katman (kW)
    minimum_exergy_kW: float
    bat_exergy_kW: float
    actual_exergy_kW: float

    # Gap hesaplamaları (kW)
    total_gap_kW: float              # actual - minimum
    bat_gap_kW: float                # actual - BAT (gerçekçi iyileştirme)
    technology_gap_kW: float         # BAT - minimum (teknoloji limiti)

    # Yüzdesel
    total_gap_pct: float
    bat_gap_pct: float
    technology_gap_pct: float

    # Spesifik tüketim
    specific_actual: float
    specific_bat: float
    specific_minimum: float
    specific_unit: str

    # Ratio
    actual_to_minimum_ratio: float
    actual_to_bat_ratio: float

    # Gap dağılımı (ekipman bazlı)
    gap_distribution: list = field(default_factory=list)

    # Ekonomik etki
    annual_total_gap_cost_eur: float = 0.0
    annual_bat_gap_cost_eur: float = 0.0
    energy_price_eur_kwh: float = 0.08
    operating_hours: float = 6000

    # BAT bilgisi
    bat_technology: str = ""
    bat_source: str = ""
    bat_efficiency_pct: float = 0.0

    # Sürdürülebilirlik skoru
    exergetic_sustainability_index: float = 0.0
    grade: str = "F"
    grade_description: str = ""

    # Hesaplama detayları
    min_exergy_method: str = ""
    min_exergy_assumptions: list = field(default_factory=list)

    # Görselleştirme verisi
    waterfall_data: dict = field(default_factory=dict)
    comparison_bar_data: dict = field(default_factory=dict)
    gap_pie_data: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """JSON serializable dict döndürür."""
        return dataclasses.asdict(self)


def analyze_gap(
    process_def,               # ProcessDefinition
    equipment_results: list,   # Ekipman analiz sonuçları
    aggregates: dict,          # Factory aggregates
    hotspots: list,            # Factory hotspots
    T0_K: float = 298.15,
    energy_price_eur_kwh: float = 0.08,
    operating_hours: float = 6000,
) -> GapAnalysisResult:
    """
    Ana gap analysis fonksiyonu.

    Adımlar:
    1. Minimum exergy hesapla (process_exergy.py)
    2. BAT exergy hesapla (bat_references.py)
    3. Mevcut exergy'yi aggregates'ten al
    4. Gap'leri hesapla
    5. Gap dağılımını ekipman bazlı çıkar
    6. ESI skoru hesapla
    7. Ekonomik etki hesapla
    8. Görselleştirme verisi üret
    """
    from engine.process_exergy import calculate_minimum_exergy
    from engine.bat_references import calculate_bat_exergy

    # Adım 1: Minimum exergy
    min_result = calculate_minimum_exergy(process_def, T0_K)
    minimum_kW = min_result["minimum_exergy_kW"]

    # Adım 2: BAT exergy
    bat_result = calculate_bat_exergy(process_def, min_result)
    bat_kW = bat_result["bat_exergy_kW"]

    # Adım 3: Mevcut exergy (factory aggregates'ten)
    actual_kW = aggregates.get("total_exergy_input_kW", 0)

    # Fallback: ekipman bazlı toplam
    if actual_kW <= 0:
        actual_kW = sum(
            _get_equipment_input(eq) for eq in equipment_results
        )

    # Minimum ve BAT'ın actual'dan büyük olmadığından emin ol
    if bat_kW >= actual_kW and actual_kW > 0:
        bat_kW = actual_kW * 0.7
    if minimum_kW >= bat_kW and bat_kW > 0:
        minimum_kW = bat_kW * 0.3

    # Adım 4: Gap hesaplamaları
    total_gap = actual_kW - minimum_kW
    bat_gap = actual_kW - bat_kW
    tech_gap = bat_kW - minimum_kW

    total_gap_pct = (total_gap / actual_kW * 100) if actual_kW > 0 else 0
    bat_gap_pct = (bat_gap / actual_kW * 100) if actual_kW > 0 else 0
    tech_gap_pct = (tech_gap / actual_kW * 100) if actual_kW > 0 else 0

    # Spesifik tüketim
    production_rate = min_result.get("production_rate_unit", 1) or 1
    specific_actual = actual_kW / production_rate if production_rate > 0 else 0

    # Ratio
    ratio_to_min = actual_kW / minimum_kW if minimum_kW > 0 else float('inf')
    ratio_to_bat = actual_kW / bat_kW if bat_kW > 0 else float('inf')

    # Adım 5: Gap dağılımı
    gap_dist = _calculate_gap_distribution(equipment_results, hotspots)

    # Adım 6: ESI skoru
    esi, grade, grade_desc = _calculate_sustainability_index(minimum_kW, actual_kW)

    # Adım 7: Ekonomik etki
    annual_total = total_gap * energy_price_eur_kwh * operating_hours
    annual_bat = bat_gap * energy_price_eur_kwh * operating_hours

    # Adım 8: Görselleştirme verisi
    waterfall = _build_waterfall_data(minimum_kW, bat_kW, actual_kW, tech_gap, gap_dist)
    comparison = _build_comparison_bar_data(minimum_kW, bat_kW, actual_kW)
    pie = _build_gap_pie_data(gap_dist)

    return GapAnalysisResult(
        process_type=process_def.process_type,
        process_label=process_def.process_label,
        subcategory=process_def.subcategory,
        minimum_exergy_kW=round(minimum_kW, 2),
        bat_exergy_kW=round(bat_kW, 2),
        actual_exergy_kW=round(actual_kW, 2),
        total_gap_kW=round(total_gap, 2),
        bat_gap_kW=round(bat_gap, 2),
        technology_gap_kW=round(tech_gap, 2),
        total_gap_pct=round(total_gap_pct, 1),
        bat_gap_pct=round(bat_gap_pct, 1),
        technology_gap_pct=round(tech_gap_pct, 1),
        specific_actual=round(specific_actual, 4),
        specific_bat=bat_result["bat_specific"],
        specific_minimum=min_result["specific_minimum"],
        specific_unit=min_result["specific_unit"],
        actual_to_minimum_ratio=round(ratio_to_min, 1),
        actual_to_bat_ratio=round(ratio_to_bat, 1),
        gap_distribution=gap_dist,
        annual_total_gap_cost_eur=round(annual_total, 0),
        annual_bat_gap_cost_eur=round(annual_bat, 0),
        energy_price_eur_kwh=energy_price_eur_kwh,
        operating_hours=operating_hours,
        bat_technology=bat_result["bat_technology"],
        bat_source=bat_result["bat_source"],
        bat_efficiency_pct=bat_result["bat_efficiency_pct"],
        exergetic_sustainability_index=esi,
        grade=grade,
        grade_description=grade_desc,
        min_exergy_method=min_result["calculation_method"],
        min_exergy_assumptions=min_result["assumptions"],
        waterfall_data=waterfall,
        comparison_bar_data=comparison,
        gap_pie_data=pie,
    )


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _get_equipment_input(eq: dict) -> float:
    """Extract exergy input from equipment result dict."""
    analysis = eq.get("analysis", eq)
    return (
        analysis.get("exergy_in_kW", 0)
        or analysis.get("fuel_exergy_kW", 0)
        or analysis.get("exergy_input_kW", 0)
        or 0
    )


def _calculate_gap_distribution(equipment_results: list, hotspots: list) -> list[dict]:
    """Ekipman bazlı gap dağılımı."""
    total_destroyed = 0.0
    for eq in equipment_results:
        analysis = eq.get("analysis", eq)
        total_destroyed += analysis.get("exergy_destroyed_kW", 0) or 0

    if total_destroyed <= 0:
        return []

    distribution = []
    cumulative = 0

    # Sort by destruction (descending)
    def _get_destroyed(eq):
        analysis = eq.get("analysis", eq)
        return analysis.get("exergy_destroyed_kW", 0) or 0

    for eq in sorted(equipment_results, key=_get_destroyed, reverse=True):
        analysis = eq.get("analysis", eq)
        destroyed = analysis.get("exergy_destroyed_kW", 0) or 0
        share = (destroyed / total_destroyed * 100) if total_destroyed > 0 else 0
        cumulative += share

        if share < 0.5:
            continue

        priority = (
            "critical" if share > 30 else
            "high" if share > 15 else
            "medium" if share > 5 else
            "low"
        )

        distribution.append({
            "equipment_name": eq.get("name", "Bilinmeyen"),
            "equipment_type": eq.get("equipment_type", "unknown"),
            "destroyed_kW": round(destroyed, 2),
            "gap_share_pct": round(share, 1),
            "cumulative_pct": round(cumulative, 1),
            "priority": priority,
        })

    return distribution


def _calculate_sustainability_index(
    minimum_kW: float, actual_kW: float
) -> tuple[float, str, str]:
    """
    Exergetic Sustainability Index.
    ESI = minimum / actual (0-1)
    """
    if actual_kW <= 0 or minimum_kW <= 0:
        return 0.0, "F", "Hesaplanamadı"

    esi = minimum_kW / actual_kW
    esi = min(1.0, max(0.0, esi))

    grades = [
        (0.50, "A", "Dünya lideri seviyesi"),
        (0.35, "B", "Çok iyi performans"),
        (0.20, "C", "İyi performans"),
        (0.10, "D", "Ortalama"),
        (0.05, "E", "Zayıf — iyileştirme gerekli"),
        (0.00, "F", "Kritik — büyük dönüşüm gerekli"),
    ]

    for threshold, grade, desc in grades:
        if esi >= threshold:
            return round(esi, 4), grade, desc

    return round(esi, 4), "F", "Kritik"


def _build_waterfall_data(min_kW, bat_kW, actual_kW, tech_gap, gap_dist) -> dict:
    """Plotly waterfall chart verisi."""
    labels = ["Minimum"]
    values = [min_kW]
    types = ["absolute"]

    # Teknoloji limiti
    labels.append("Teknoloji Limiti")
    values.append(tech_gap)
    types.append("relative")

    # Top 5 ekipman gap
    for eq in gap_dist[:5]:
        labels.append(eq["equipment_name"])
        values.append(eq["destroyed_kW"])
        types.append("relative")

    # Toplam
    labels.append("Mevcut Tesis")
    values.append(actual_kW)
    types.append("total")

    return {
        "labels": labels,
        "values": [round(v, 1) for v in values],
        "types": types,
    }


def _build_comparison_bar_data(min_kW, bat_kW, actual_kW) -> dict:
    """3 katman bar chart verisi."""
    return {
        "categories": ["Termodinamik\nMinimum", "BAT\nReferans", "Mevcut\nTesis"],
        "values": [round(min_kW, 1), round(bat_kW, 1), round(actual_kW, 1)],
        "colors": ["#10B981", "#F59E0B", "#EF4444"],
    }


def _build_gap_pie_data(gap_dist) -> dict:
    """Gap dağılımı donut chart verisi."""
    labels = [eq["equipment_name"] for eq in gap_dist[:7]]
    values = [eq["destroyed_kW"] for eq in gap_dist[:7]]

    if len(gap_dist) > 7:
        labels.append("Diğer")
        values.append(sum(eq["destroyed_kW"] for eq in gap_dist[7:]))

    return {"labels": labels, "values": [round(v, 1) for v in values]}
