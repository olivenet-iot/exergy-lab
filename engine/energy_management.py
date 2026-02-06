"""
ExergyLab - ISO 50001 Energy Management Motor Modulu

Fabrika seviyesi enerji yonetimi degerlendirmesi:
  - 7 Energy Performance Indicator (EnPI) hesaplama
  - 7 boyutlu olgunluk skorlamasi (ISO 50001 maddeleri bazinda)
  - Bosluk analizi (gap analysis) ve kapama onerileri
  - Tum motorlardan birlesik eylem plani olusturma
  - Radar chart ve timeline gorsellestirme verisi

Bu, ExergyLab'in 6. ve son analiz motorudur. Diger motorlardan
farkli olarak, hesaplama yapmaz — onceki tum sonuclari sentezler.

Referanslar:
  - ISO 50001:2018 Energy management systems
  - Tsatsaronis, G. (2006). "Definitions and nomenclature in exergy analysis"
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MATURITY_LEVELS = {
    "leading":    {"min": 90, "label": "Lider (Leading)", "description": "ISO 50001 sertifikasyona hazir"},
    "mature":     {"min": 70, "label": "Olgun (Mature)", "description": "Ileri duzey enerji yonetimi"},
    "developing": {"min": 50, "label": "Gelisen (Developing)", "description": "Temel enerji yonetimi mevcut"},
    "beginning":  {"min": 30, "label": "Baslangic (Beginning)", "description": "Bazi uygulamalar var"},
    "aware":      {"min": 0,  "label": "Farkindalik (Aware)", "description": "Minimum enerji yonetimi"},
}

MATURITY_DIMENSIONS = {
    "energy_review": {
        "label": "Enerji Gozden Gecirmesi",
        "iso_clause": "6.3",
        "description": "Enerji kullaniminin ve tuketiminin analizi",
    },
    "performance_indicators": {
        "label": "Performans Gostergeleri",
        "iso_clause": "6.5",
        "description": "EnPI tanimlama ve izleme",
    },
    "improvement_opportunities": {
        "label": "Iyilestirme Firsatlari",
        "iso_clause": "6.4",
        "description": "Iyilestirme firsatlarinin belirlenmesi ve onceliklendirilmesi",
    },
    "action_planning": {
        "label": "Aksiyon Planlama",
        "iso_clause": "6.6",
        "description": "Eylem planlarinin olusturulmasi",
    },
    "monitoring": {
        "label": "Izleme ve Olcme",
        "iso_clause": "9.1",
        "description": "Performans izleme ve olcme altyapisi",
    },
    "heat_integration": {
        "label": "Isi Entegrasyonu",
        "iso_clause": "6.4",
        "description": "Isi geri kazanim ve entegrasyon firsatlari",
    },
    "cost_optimization": {
        "label": "Maliyet Optimizasyonu",
        "iso_clause": "6.5",
        "description": "Enerji maliyetlerinin optimizasyonu",
    },
}

ACTION_CATEGORIES = {
    "quick_win":   {"label": "Hizli Kazanim", "timeline": "0-3 ay", "color": "#22c55e"},
    "medium_term": {"label": "Orta Vadeli", "timeline": "3-12 ay", "color": "#f59e0b"},
    "strategic":   {"label": "Stratejik", "timeline": "1-3 yil", "color": "#8b5cf6"},
    "monitoring":  {"label": "Izleme", "timeline": "Surekli", "color": "#3b82f6"},
}

GAP_RECOMMENDATIONS = {
    "energy_review": [
        "Tum enerji tuketen ekipmanlari envantere ekleyin",
        "Eksik ekipman tiplerini (pompa, HX, vb.) analiz kapsamina alin",
        "Duzenli enerji gozden gecirmesi proseduru olusturun",
    ],
    "performance_indicators": [
        "Exergoekonomik analizi tum ekipmanlara uygulayin",
        "EnPI hedeflerini belirleyin ve izleme sistemini kurun",
        "Aylik EnPI raporlama proseduru olusturun",
    ],
    "improvement_opportunities": [
        "Kacinilabilir/kacinilmaz analizi yapin",
        "Endojen/eksojen dekompozisyonu uygulayin",
        "Entropi uretimi analizi ile tersinmezlik kaynaklarini belirleyin",
    ],
    "action_planning": [
        "Termoekonomik optimizasyon analizi calistirin",
        "Her ekipman icin maliyet-fayda degerlendirmesi yapin",
        "Yillik enerji iyilestirme hedefleri belirleyin",
    ],
    "monitoring": [
        "Gercek zamanli enerji izleme sistemi kurun",
        "Kritik ekipmanlara alt olcum cihazlari ekleyin",
        "Entropi uretimi bazli performans takibi uygulayin",
    ],
    "heat_integration": [
        "Pinch analizi ile isi entegrasyonu firsatlarini belirleyin",
        "Atik isi geri kazanim projelerini degerlendirin",
        "Isi esanjor agi optimizasyonu yapin",
    ],
    "cost_optimization": [
        "SPECO analizi ile maliyet dagilimini belirleyin",
        "f-faktor/r-faktor bazli optimizasyon stratejileri uygulayin",
        "Yatirim geri donus analizlerini tamamlayin",
    ],
}


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class EnPIMetrics:
    """Energy Performance Indicators."""
    exergy_efficiency_pct: float          # eta_ex_factory
    specific_exergy_consumption: float    # SEC (kW/kW)
    exergy_destruction_ratio_pct: float   # EDR (%)
    avoidable_loss_ratio_pct: float       # ALR (%)
    energy_cost_intensity_eur_kWh: float  # ECI (EUR/kWh)
    heat_recovery_potential_pct: float    # HRP (%)
    entropy_generation_intensity: float   # EGI (= N_s_factory)

    def to_dict(self) -> dict:
        return {
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "specific_exergy_consumption": round(self.specific_exergy_consumption, 3),
            "exergy_destruction_ratio_pct": round(self.exergy_destruction_ratio_pct, 1),
            "avoidable_loss_ratio_pct": round(self.avoidable_loss_ratio_pct, 1),
            "energy_cost_intensity_eur_kWh": round(self.energy_cost_intensity_eur_kWh, 4),
            "heat_recovery_potential_pct": round(self.heat_recovery_potential_pct, 1),
            "entropy_generation_intensity": round(self.entropy_generation_intensity, 4),
        }


@dataclass
class MaturityDimension:
    """Tek boyut olgunluk skoru."""
    dimension: str
    label: str
    iso_clause: str
    score: int                 # 0-100
    max_score: int             # 100
    findings: List[str]        # Ne bulundu
    gaps: List[str]            # Ne eksik

    def to_dict(self) -> dict:
        return {
            "dimension": self.dimension,
            "label": self.label,
            "iso_clause": self.iso_clause,
            "score": self.score,
            "max_score": self.max_score,
            "findings": self.findings,
            "gaps": self.gaps,
        }


@dataclass
class ActionItem:
    """Eylem plani kalemi."""
    id: str
    source: str
    equipment_id: Optional[str]
    equipment_name: Optional[str]
    action: str
    category: str              # quick_win | medium_term | strategic | monitoring
    estimated_savings_eur: float
    estimated_investment_eur: float
    payback_years: float
    priority: str
    timeline: str

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "source": self.source,
            "equipment_id": self.equipment_id,
            "equipment_name": self.equipment_name,
            "action": self.action,
            "category": self.category,
            "estimated_savings_eur": round(self.estimated_savings_eur, 2),
            "estimated_investment_eur": round(self.estimated_investment_eur, 2),
            "payback_years": round(self.payback_years, 1),
            "priority": self.priority,
            "timeline": self.timeline,
        }


@dataclass
class EnergyManagementResult:
    """Fabrika seviyesi ISO 50001 enerji yonetimi sonucu."""
    is_valid: bool = True
    error_message: str = ""

    num_equipment: int = 0

    # EnPI'ler
    enpi: Optional[EnPIMetrics] = None

    # Olgunluk degerlendirmesi
    maturity_score: int = 0                          # Toplam ortalama (0-100)
    maturity_level: str = "aware"                    # leading | mature | developing | beginning | aware
    maturity_level_label: str = "Farkindalik (Aware)"
    maturity_dimensions: List[MaturityDimension] = field(default_factory=list)

    # Bosluk analizi
    num_gaps: int = 0
    critical_gaps: List[str] = field(default_factory=list)  # Skor < 50 olan boyutlar

    # Eylem plani
    action_plan: List[ActionItem] = field(default_factory=list)
    action_summary: Dict = field(default_factory=dict)
    total_potential_savings_eur: float = 0.0
    total_estimated_investment_eur: float = 0.0

    # Gorsellestirme
    enpi_radar_data: Dict = field(default_factory=dict)
    maturity_radar_data: Dict = field(default_factory=dict)
    action_timeline_data: Dict = field(default_factory=dict)

    # Uyarilar
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "is_valid": self.is_valid,
            "error_message": self.error_message,
            "num_equipment": self.num_equipment,
            "enpi": self.enpi.to_dict() if self.enpi else {},
            "maturity_score": self.maturity_score,
            "maturity_level": self.maturity_level,
            "maturity_level_label": self.maturity_level_label,
            "maturity_dimensions": [d.to_dict() for d in self.maturity_dimensions],
            "num_gaps": self.num_gaps,
            "critical_gaps": self.critical_gaps,
            "action_plan": [a.to_dict() for a in self.action_plan],
            "action_summary": self.action_summary,
            "total_potential_savings_eur": round(self.total_potential_savings_eur, 2),
            "total_estimated_investment_eur": round(self.total_estimated_investment_eur, 2),
            "enpi_radar_data": self.enpi_radar_data,
            "maturity_radar_data": self.maturity_radar_data,
            "action_timeline_data": self.action_timeline_data,
            "warnings": self.warnings,
        }


# ---------------------------------------------------------------------------
# EnPI Calculation
# ---------------------------------------------------------------------------

def _get_analysis(eq_result: dict) -> dict:
    """Extract analysis dict from equipment result (handles nested or flat)."""
    analysis = eq_result.get("analysis")
    if isinstance(analysis, dict):
        return analysis
    return eq_result


def _calculate_enpi(factory_data: dict) -> EnPIMetrics:
    """Mevcut fabrika verisinden EnPI'ler hesapla.

    Args:
        factory_data: Factory analysis dict with aggregates, equipment_results,
            entropy_generation etc.

    Returns:
        EnPIMetrics with 7 performance indicators.
    """
    agg = factory_data.get("aggregates", {})
    eq_results = factory_data.get("equipment_results", [])
    egm = factory_data.get("entropy_generation")

    E_x_in = agg.get("total_exergy_input_kW", 0) or 0
    E_x_out = agg.get("total_exergy_output_kW", 0) or 0
    I_total = agg.get("total_exergy_destroyed_kW", 0) or 0

    # 1. eta_ex_factory
    eta_ex = (E_x_out / E_x_in * 100) if E_x_in > 0 else 0.0

    # 2. SEC = E_x_in / E_x_out
    sec = (E_x_in / E_x_out) if E_x_out > 0 else 0.0

    # 3. EDR = I_total / E_x_in * 100
    edr = (I_total / E_x_in * 100) if E_x_in > 0 else 0.0

    # 4. ALR = I_avoidable / I_total * 100
    I_avoidable = 0.0
    for r in eq_results:
        a = _get_analysis(r)
        I_avoidable += (a.get("exergy_destroyed_avoidable_kW") or 0)
    alr = (I_avoidable / I_total * 100) if I_total > 0 else 0.0

    # 5. ECI = C_dot_D_total / E_x_in
    C_dot_D_total = 0.0
    for r in eq_results:
        a = _get_analysis(r)
        C_dot_D_total += (a.get("exergoeconomic_C_dot_destruction_eur_h") or 0)
    eci = (C_dot_D_total / E_x_in) if E_x_in > 0 else 0.0

    # 6. HRP = recoverable / I_total * 100
    recoverable = 0.0
    for r in eq_results:
        a = _get_analysis(r)
        recoverable += (a.get("recoverable_heat_kW") or 0)
    hrp = (recoverable / I_total * 100) if I_total > 0 else 0.0

    # 7. EGI = N_s_factory (from EGM)
    egi = 0.0
    if egm and isinstance(egm, dict):
        egi = egm.get("N_s_factory", 0) or 0

    return EnPIMetrics(
        exergy_efficiency_pct=eta_ex,
        specific_exergy_consumption=sec,
        exergy_destruction_ratio_pct=edr,
        avoidable_loss_ratio_pct=alr,
        energy_cost_intensity_eur_kWh=eci,
        heat_recovery_potential_pct=hrp,
        entropy_generation_intensity=egi,
    )


# ---------------------------------------------------------------------------
# Maturity Scorers
# ---------------------------------------------------------------------------

def _score_energy_review(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """6.3 - Enerji gozden gecirmesi skoru (0-100)."""
    score = 0
    findings = []
    gaps = []

    eq_results = factory_data.get("equipment_results", [])
    n_eq = len(eq_results)
    types = set()
    for r in eq_results:
        t = r.get("equipment_type")
        if not t:
            a = _get_analysis(r)
            t = a.get("equipment_type")
        if t:
            types.add(t)

    # Ekipman sayisi (max 25 puan)
    eq_score = min(25, n_eq * 5)
    score += eq_score
    if n_eq > 0:
        findings.append(f"{n_eq} ekipman analiz edildi")
    if n_eq < 3:
        gaps.append("Daha fazla ekipman analiz kapsamina alinmali")

    # Ekipman cesitliligi (max 25 puan)
    type_score = min(25, len(types) * 7)
    score += type_score
    if len(types) > 1:
        findings.append(f"{len(types)} farkli ekipman tipi mevcut")
    if len(types) < 3:
        gaps.append("Ekipman tip cesitliligi artirilmali")

    # AV/UN analizi (25 puan)
    has_avun = any(
        _get_analysis(r).get("avoidable_ratio_pct") is not None
        for r in eq_results
    )
    if has_avun:
        score += 25
        findings.append("Kacinilabilir/kacinilmaz analizi mevcut")
    else:
        gaps.append("AV/UN analizi yapilmali")

    # EN/EX veya EGM (25 puan)
    has_advanced = (
        factory_data.get("advanced_exergy") is not None
        or factory_data.get("entropy_generation") is not None
    )
    if has_advanced:
        score += 25
        findings.append("Ileri duzey exergy analizi mevcut")
    else:
        gaps.append("Ileri duzey analiz (EN/EX veya EGM) yapilmali")

    return score, findings, gaps


def _score_performance_indicators(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """6.5 - Performans gostergeleri skoru (0-100)."""
    score = 0
    findings = []
    gaps = []
    eq_results = factory_data.get("equipment_results", [])

    # Exergy verimi hesaplanmis (25 puan)
    has_eta = any(
        _get_analysis(r).get("exergy_efficiency_pct") is not None
        for r in eq_results
    )
    if has_eta:
        score += 25
        findings.append("Exergy verimlilikleri hesaplanmis")
    else:
        gaps.append("Exergy verimi hesaplanmali")

    # Exergoekonomik analiz (25 puan)
    has_speco = any(
        _get_analysis(r).get("exergoeconomic_f_factor") is not None
        for r in eq_results
    )
    if has_speco:
        score += 25
        findings.append("SPECO analizi mevcut")
    else:
        gaps.append("Exergoekonomik analiz yapilmali")

    # Benchmark karsilastirma (25 puan)
    has_benchmark = any(
        _get_analysis(r).get("benchmark_rating") is not None
        for r in eq_results
    )
    if has_benchmark:
        score += 25
        findings.append("Sektor benchmark karsilastirmasi mevcut")
    else:
        gaps.append("Benchmark karsilastirmasi yapilmali")

    # Cok ekipmanli izleme (25 puan)
    if len(eq_results) >= 3:
        score += 25
        findings.append(f"{len(eq_results)} ekipman izleniyor")
    else:
        gaps.append("En az 3 ekipman izlenmeli")

    return score, findings, gaps


def _score_improvement_opportunities(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """6.4 - Iyilestirme firsatlari skoru (0-100)."""
    score = 0
    findings = []
    gaps = []

    eq_results = factory_data.get("equipment_results", [])

    # AV/UN mevcut (25)
    has_avun = any(
        _get_analysis(r).get("avoidable_ratio_pct") is not None
        for r in eq_results
    )
    if has_avun:
        score += 25
        findings.append("Kacinilabilir kayip analizi mevcut")
    else:
        gaps.append("AV/UN analizi yapilmali")

    # EN/EX mevcut (25)
    if factory_data.get("advanced_exergy"):
        score += 25
        findings.append("EN/EX dekompozisyon mevcut")
    else:
        gaps.append("Endojen/eksojen analizi yapilmali")

    # EGM mevcut (25)
    if factory_data.get("entropy_generation"):
        score += 25
        findings.append("Entropi uretimi analizi mevcut")
    else:
        gaps.append("EGM analizi yapilmali")

    # Pinch analizi (25)
    if factory_data.get("pinch_analysis"):
        score += 25
        findings.append("Pinch analizi mevcut")
    else:
        gaps.append("Pinch analizi yapilmali")

    return score, findings, gaps


def _score_action_planning(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """6.6 - Aksiyon planlama skoru (0-100)."""
    score = 0
    findings = []
    gaps = []

    thermo = factory_data.get("thermoeconomic_optimization")
    if thermo and thermo.get("is_valid"):
        score += 50
        findings.append("Termoekonomik optimizasyon mevcut")

        # ROI analizi var mi (25)
        ranking = thermo.get("cost_benefit_ranking", [])
        if ranking:
            score += 25
            findings.append(f"{len(ranking)} ekipman icin ROI analizi yapilmis")
        else:
            gaps.append("Maliyet-fayda siralamasi olusturulmali")

        # Coklu strateji (25)
        dist = thermo.get("strategy_distribution", {})
        if len(dist) > 1:
            score += 25
            findings.append("Coklu optimizasyon stratejisi belirlenmis")
        else:
            gaps.append("Farkli ekipmanlar icin farkli stratejiler degerlendirilmeli")
    else:
        gaps.append("Termoekonomik optimizasyon analizi yapilmali")

    return score, findings, gaps


def _score_monitoring(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """9.1 - Izleme ve olcme skoru (0-100)."""
    score = 0
    findings = []
    gaps = []

    eq_results = factory_data.get("equipment_results", [])
    n_eq = len(eq_results)

    # Ekipman verisi var (25)
    if n_eq > 0:
        score += 25
        findings.append(f"{n_eq} ekipman icin veri mevcut")
    else:
        gaps.append("Ekipman verileri girilmeli")

    # EGM analizi (25) — entropi takibi
    if factory_data.get("entropy_generation"):
        score += 25
        findings.append("Entropi bazli izleme mevcut")
    else:
        gaps.append("Entropi uretimi izlemesi kurulmali")

    # Veri kalitesi — exergy_in > 0 olanlarin orani (25)
    valid = sum(
        1 for r in eq_results
        if (_get_analysis(r).get("exergy_in_kW") or 0) > 0
    )
    quality_ratio = valid / n_eq if n_eq > 0 else 0
    quality_score = int(quality_ratio * 25)
    score += quality_score
    if quality_ratio > 0.8:
        findings.append("Veri kalitesi iyi")
    else:
        gaps.append("Bazi ekipmanlarin exergy verileri eksik")

    # Coklu analiz katmani (25) — 3+ motor calisiyorsa
    motors_available = sum(
        1 for k in [
            "pinch_analysis", "advanced_exergy",
            "entropy_generation", "thermoeconomic_optimization",
        ]
        if factory_data.get(k) is not None
    )
    motor_score = min(25, motors_available * 8)
    score += motor_score
    if motors_available >= 3:
        findings.append(f"{motors_available} analiz motoru aktif")
    else:
        gaps.append("Daha fazla analiz motoru etkinlestirilmeli")

    return score, findings, gaps


def _score_heat_integration(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """6.4 - Isi entegrasyonu skoru (0-100)."""
    score = 0
    findings = []
    gaps = []

    pinch = factory_data.get("pinch_analysis")
    if pinch and pinch.get("is_valid"):
        score += 50
        findings.append("Pinch analizi tamamlanmis")

        # Isi geri kazanim potansiyeli var (25)
        recovery = pinch.get("max_heat_recovery_kW", 0) or 0
        if recovery > 0:
            score += 25
            findings.append(f"Isi geri kazanim potansiyeli: {recovery:.0f} kW")

        # Minimum yardimci isitma/sogutma hesaplanmis (25)
        if pinch.get("hot_utility_kW") is not None:
            score += 25
            findings.append("Minimum yardimci isitma/sogutma belirlenmis")
    else:
        gaps.append("Pinch analizi yapilmali")

        # Isi esanjoru var mi (kismi puan)
        eq_results = factory_data.get("equipment_results", [])
        hx_count = sum(
            1 for r in eq_results
            if r.get("equipment_type") == "heat_exchanger"
        )
        if hx_count > 0:
            score += 15
            findings.append(f"{hx_count} isi esanjoru mevcut")
        else:
            gaps.append("Isi esanjoru eklenmeli")

    return score, findings, gaps


def _score_cost_optimization(factory_data: dict) -> Tuple[int, List[str], List[str]]:
    """6.5 - Maliyet optimizasyonu skoru (0-100)."""
    score = 0
    findings = []
    gaps = []

    eq_results = factory_data.get("equipment_results", [])

    # SPECO mevcut (35)
    has_speco = any(
        _get_analysis(r).get("exergoeconomic_f_factor") is not None
        for r in eq_results
    )
    if has_speco:
        score += 35
        findings.append("Exergoekonomik maliyet analizi mevcut")
    else:
        gaps.append("SPECO analizi yapilmali")

    # Termoekonomik optimizasyon (35)
    thermo = factory_data.get("thermoeconomic_optimization")
    if thermo and thermo.get("is_valid"):
        score += 35
        findings.append("Optimizasyon stratejileri belirlenmis")

        savings = thermo.get("total_savings_annual_eur", 0) or 0
        if savings > 0:
            findings.append(f"Toplam tasarruf potansiyeli: {savings:,.0f} EUR/yil")
    else:
        gaps.append("Termoekonomik optimizasyon yapilmali")

    # Maliyet bazli siralama (30)
    if thermo and thermo.get("cost_benefit_ranking"):
        score += 30
        findings.append("Maliyet-fayda siralamasi mevcut")
    else:
        gaps.append("ROI bazli onceliklendirme yapilmali")

    return score, findings, gaps


# Scorer registry
MATURITY_SCORERS = {
    "energy_review": _score_energy_review,
    "performance_indicators": _score_performance_indicators,
    "improvement_opportunities": _score_improvement_opportunities,
    "action_planning": _score_action_planning,
    "monitoring": _score_monitoring,
    "heat_integration": _score_heat_integration,
    "cost_optimization": _score_cost_optimization,
}


# ---------------------------------------------------------------------------
# Maturity Assessment
# ---------------------------------------------------------------------------

def _assess_maturity(factory_data: dict) -> List[MaturityDimension]:
    """7 boyutta olgunluk skorlamasi."""
    dimensions = []

    for dim_key, dim_info in MATURITY_DIMENSIONS.items():
        scorer = MATURITY_SCORERS.get(dim_key)
        if scorer:
            score, findings, gaps = scorer(factory_data)
        else:
            score, findings, gaps = 0, [], ["Degerlendirme mevcut degil"]

        dimensions.append(MaturityDimension(
            dimension=dim_key,
            label=dim_info["label"],
            iso_clause=dim_info["iso_clause"],
            score=min(100, max(0, score)),
            max_score=100,
            findings=findings,
            gaps=gaps,
        ))

    return dimensions


def _determine_maturity_level(score: int) -> Tuple[str, str]:
    """Olgunluk seviyesini belirle.

    Returns:
        (level_key, label) tuple.
    """
    for level, info in MATURITY_LEVELS.items():
        if score >= info["min"]:
            return level, info["label"]
    return "aware", MATURITY_LEVELS["aware"]["label"]


# ---------------------------------------------------------------------------
# Action Plan
# ---------------------------------------------------------------------------

def _build_action_plan(factory_data: dict) -> List[ActionItem]:
    """Tum motorlardan gelen onerileri birlestirip eylem plani olustur."""
    actions: List[ActionItem] = []
    counter = 1

    # 1. Termoekonomik optimizasyondan aksiyonlar
    thermo = factory_data.get("thermoeconomic_optimization")
    if thermo and thermo.get("is_valid"):
        for rec in thermo.get("recommendations", []):
            if rec.get("strategy") == "maintain":
                category = "monitoring"
                timeline = "Surekli"
            elif (rec.get("simple_payback_years") or 99) < 1:
                category = "quick_win"
                timeline = "0-3 ay"
            elif (rec.get("simple_payback_years") or 99) < 3:
                category = "medium_term"
                timeline = "3-12 ay"
            else:
                category = "strategic"
                timeline = "1-3 yil"

            rec_actions = rec.get("recommended_actions", ["Degerlendirme yapin"])
            action_text = rec_actions[0] if rec_actions else "Degerlendirme yapin"

            actions.append(ActionItem(
                id=f"A-{counter:02d}",
                source="thermoeconomic",
                equipment_id=rec.get("equipment_id"),
                equipment_name=rec.get("equipment_name"),
                action=action_text,
                category=category,
                estimated_savings_eur=rec.get("C_savings_annual_eur", 0) or 0,
                estimated_investment_eur=rec.get("estimated_investment_eur", 0) or 0,
                payback_years=rec.get("simple_payback_years", 99.9) or 99.9,
                priority=rec.get("priority", "medium"),
                timeline=timeline,
            ))
            counter += 1

    # 2. Pinch analizinden aksiyonlar
    pinch = factory_data.get("pinch_analysis")
    if pinch and pinch.get("is_valid"):
        recovery_kW = pinch.get("max_heat_recovery_kW", 0) or 0
        if recovery_kW > 0:
            savings = recovery_kW * 8000 * 0.05  # 8000h/yil, 0.05 EUR/kWh
            investment = recovery_kW * 200        # 200 EUR/kW HX maliyeti
            payback = investment / savings if savings > 0 else 99.9

            actions.append(ActionItem(
                id=f"A-{counter:02d}",
                source="pinch",
                equipment_id=None,
                equipment_name=None,
                action=f"Pinch analizi sonuclarina gore isi entegrasyonu yapin ({recovery_kW:.0f} kW potansiyel)",
                category="medium_term" if payback < 3 else "strategic",
                estimated_savings_eur=savings,
                estimated_investment_eur=investment,
                payback_years=min(payback, 99.9),
                priority="high" if recovery_kW > 100 else "medium",
                timeline="3-12 ay" if payback < 3 else "1-3 yil",
            ))
            counter += 1

    # Sort: quick_win -> medium_term -> strategic -> monitoring, then payback
    category_order = {"quick_win": 0, "medium_term": 1, "strategic": 2, "monitoring": 3}
    actions.sort(key=lambda a: (category_order.get(a.category, 4), a.payback_years))

    return actions


def _summarize_actions(actions: List[ActionItem]) -> dict:
    """Eylem plani ozeti."""
    summary = {}
    for cat_key, cat_info in ACTION_CATEGORIES.items():
        cat_actions = [a for a in actions if a.category == cat_key]
        summary[cat_key] = {
            "count": len(cat_actions),
            "label": cat_info["label"],
            "total_savings_eur": round(sum(a.estimated_savings_eur for a in cat_actions), 2),
            "total_investment_eur": round(sum(a.estimated_investment_eur for a in cat_actions), 2),
        }
    return summary


# ---------------------------------------------------------------------------
# Chart Data Generation
# ---------------------------------------------------------------------------

def _generate_enpi_radar(enpi: EnPIMetrics) -> dict:
    """EnPI radar chart verisi (0-100 normalize)."""
    return {
        "categories": [
            "Exergy Verimi", "SEC", "Yikim Orani", "Kacinilabilir Kayip",
            "Maliyet Yogunlugu", "Isi Geri Kazanim", "Entropi Yogunlugu",
        ],
        "values": [
            min(100, max(0, enpi.exergy_efficiency_pct)),
            min(100, max(0, (3 - enpi.specific_exergy_consumption) / 3 * 100)),
            min(100, max(0, 100 - enpi.exergy_destruction_ratio_pct)),
            min(100, max(0, enpi.avoidable_loss_ratio_pct)),
            min(100, max(0, 100 - enpi.energy_cost_intensity_eur_kWh * 1000)),
            min(100, max(0, enpi.heat_recovery_potential_pct)),
            min(100, max(0, 100 - enpi.entropy_generation_intensity * 100)),
        ],
    }


def _generate_maturity_radar(dimensions: List[MaturityDimension]) -> dict:
    """Olgunluk radar chart verisi."""
    return {
        "categories": [d.label for d in dimensions],
        "values": [d.score for d in dimensions],
        "max_value": 100,
    }


def _generate_action_timeline(actions: List[ActionItem]) -> dict:
    """Eylem plani timeline chart verisi."""
    categories: Dict[str, list] = {
        "quick_win": [], "medium_term": [], "strategic": [], "monitoring": [],
    }
    for a in actions:
        bucket = categories.get(a.category)
        if bucket is not None:
            bucket.append({
                "id": a.id,
                "action": a.action[:50],
                "equipment": a.equipment_name or "Fabrika",
                "savings": a.estimated_savings_eur,
                "priority": a.priority,
            })
    return {
        "categories": {k: v for k, v in categories.items() if v},
        "category_labels": {k: v["label"] for k, v in ACTION_CATEGORIES.items()},
        "category_colors": {k: v["color"] for k, v in ACTION_CATEGORIES.items()},
    }


# ---------------------------------------------------------------------------
# Warnings
# ---------------------------------------------------------------------------

def _collect_warnings(
    enpi: EnPIMetrics,
    maturity_score: int,
    actions: List[ActionItem],
) -> List[str]:
    """Uyarilar topla."""
    warnings = []
    if maturity_score < 30:
        warnings.append("Enerji yonetim olgunlugu cok dusuk — temel adimlarla baslayin")
    if enpi.exergy_destruction_ratio_pct > 60:
        warnings.append(
            f"Cok yuksek exergy yikim orani: %{enpi.exergy_destruction_ratio_pct:.0f}"
        )
    if not actions:
        warnings.append(
            "Aksiyon plani olusturulamadi — termoekonomik optimizasyon calistirin"
        )
    if enpi.avoidable_loss_ratio_pct > 50:
        warnings.append(
            f"Yuksek kacinilabilir kayip orani: %{enpi.avoidable_loss_ratio_pct:.0f} — hizli kazanimlar oncelikli"
        )
    return warnings


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def check_energy_management_feasibility(
    factory_data: dict,
) -> Tuple[bool, List[str]]:
    """Check if energy management assessment is feasible.

    Requirements:
    - At least 1 equipment result

    Returns:
        (feasible, reasons)
    """
    eq = factory_data.get("equipment_results", [])
    if len(eq) < 1:
        return False, ["Ekipman sonucu yok"]
    return True, [f"Uygun: {len(eq)} ekipman"]


def analyze_energy_management(
    factory_data: dict,
) -> EnergyManagementResult:
    """ISO 50001 enerji yonetimi degerlendirmesi.

    Args:
        factory_data: Factory analysis dict (from FactoryAnalysisResult fields).
            Contains: equipment_results, aggregates, hotspots,
            pinch_analysis, advanced_exergy, entropy_generation,
            thermoeconomic_optimization.

    Returns:
        EnergyManagementResult with EnPI, maturity, action plan, charts.
    """
    equipment_results = factory_data.get("equipment_results", [])
    if not equipment_results:
        return EnergyManagementResult(
            is_valid=False,
            error_message="Ekipman sonucu yok",
        )

    # 1. EnPI hesapla
    enpi = _calculate_enpi(factory_data)

    # 2. Olgunluk degerlendirmesi
    dimensions = _assess_maturity(factory_data)
    if dimensions:
        maturity_score = sum(d.score for d in dimensions) // len(dimensions)
    else:
        maturity_score = 0
    maturity_level, maturity_label = _determine_maturity_level(maturity_score)

    # 3. Bosluk analizi
    gap_dimensions = [d for d in dimensions if d.score < 70]
    num_gaps = len(gap_dimensions)
    critical_gaps = [d.label for d in dimensions if d.score < 50]

    # 4. Eylem plani
    action_plan = _build_action_plan(factory_data)
    action_summary = _summarize_actions(action_plan)
    total_savings = sum(a.estimated_savings_eur for a in action_plan)
    total_investment = sum(a.estimated_investment_eur for a in action_plan)

    # 5. Gorsellestirme verileri
    enpi_radar = _generate_enpi_radar(enpi)
    maturity_radar = _generate_maturity_radar(dimensions)
    timeline_data = _generate_action_timeline(action_plan)

    # 6. Uyarilar
    warnings = _collect_warnings(enpi, maturity_score, action_plan)

    return EnergyManagementResult(
        num_equipment=len(equipment_results),
        enpi=enpi,
        maturity_score=maturity_score,
        maturity_level=maturity_level,
        maturity_level_label=maturity_label,
        maturity_dimensions=dimensions,
        num_gaps=num_gaps,
        critical_gaps=critical_gaps,
        action_plan=action_plan,
        action_summary=action_summary,
        total_potential_savings_eur=total_savings,
        total_estimated_investment_eur=total_investment,
        enpi_radar_data=enpi_radar,
        maturity_radar_data=maturity_radar,
        action_timeline_data=timeline_data,
        warnings=warnings,
    )
