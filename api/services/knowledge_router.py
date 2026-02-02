"""Topic-based knowledge file router for AI chat.

Routes user questions to the most relevant knowledge files based on
keyword matching across Turkish and English terms.
"""

import logging
import os
from pathlib import Path
from typing import List, Optional

logger = logging.getLogger(__name__)

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
_KNOWLEDGE_DIR = _PROJECT_ROOT / "knowledge"


# ---------------------------------------------------------------------------
# Helper functions (defined before TOPIC_ROUTES which reference them)
# ---------------------------------------------------------------------------

def _glob_knowledge(subpath: str, max_files: int = 6) -> List[str]:
    """List .md files in a knowledge subdirectory.

    Args:
        subpath: Relative path under knowledge/ (e.g. 'compressor/solutions')
        max_files: Maximum number of files to return.

    Returns:
        List of relative paths from project root (e.g. 'knowledge/compressor/solutions/vsd.md')
    """
    target_dir = _KNOWLEDGE_DIR / subpath
    if not target_dir.is_dir():
        return []
    files = sorted(target_dir.glob("*.md"))
    return [f"knowledge/{subpath}/{f.name}" for f in files[:max_files]]


def _match_sector_files(question: str) -> List[str]:
    """Detect sector keywords in the question and return matching sector files."""
    question_lower = question.lower()
    matched: List[str] = []
    for keyword, file_path in SECTOR_MAP.items():
        if keyword in question_lower and file_path not in matched:
            matched.append(file_path)
    return matched


# ---------------------------------------------------------------------------
# Topic routes — each entry maps keywords to knowledge file paths
# ---------------------------------------------------------------------------

TOPIC_ROUTES = [
    {
        "topic": "solutions",
        "keywords_tr": ["iyileştirme", "iyilestirme", "çözüm", "cozum", "öneri", "oneri", "tasarruf", "verim artırma"],
        "keywords_en": ["improvement", "solution", "recommendation", "saving", "optimization"],
        "files_equipment": lambda eq: _glob_knowledge(f"{eq}/solutions"),
        "files_factory": [],
    },
    {
        "topic": "audit",
        "keywords_tr": ["denetim", "ölçüm", "olcum", "veri toplama", "saha"],
        "keywords_en": ["audit", "measurement", "data collection", "field"],
        "files_equipment": lambda eq: [f"knowledge/{eq}/audit.md"],
        "files_factory": ["knowledge/factory/data_collection.md", "knowledge/factory/methodology.md"],
    },
    {
        "topic": "pinch",
        "keywords_tr": ["pinch", "ısı entegrasyonu", "isi entegrasyonu", "composite", "hen", "ısı değiştirici ağı"],
        "keywords_en": ["pinch", "heat integration", "composite curve", "hen design"],
        "files_equipment": lambda eq: [],
        "files_factory": lambda: _glob_knowledge("factory/pinch"),
    },
    {
        "topic": "economics",
        "keywords_tr": ["maliyet", "yatırım", "yatirim", "geri ödeme", "geri odeme", "ekonomik", "fiyat", "bütçe"],
        "keywords_en": ["cost", "investment", "payback", "economic", "price", "budget", "roi"],
        "files_equipment": lambda eq: [f"knowledge/{eq}/benchmarks.md"],
        "files_factory": [
            "knowledge/factory/economic_analysis.md",
            "knowledge/factory/life_cycle_cost.md",
            "knowledge/factory/exergoeconomic/evaluation_criteria.md",
            "knowledge/factory/exergoeconomic/overview.md",
        ],
    },
    {
        "topic": "entropy",
        "keywords_tr": ["entropi", "bejan", "gouy", "stodola", "tersinmezlik", "geri dönüşümsüzlük"],
        "keywords_en": ["entropy", "bejan", "gouy", "stodola", "irreversibility", "egm"],
        "files_equipment": lambda eq: [],
        "files_factory": lambda: _glob_knowledge("factory/entropy_generation"),
    },
    {
        "topic": "advanced_exergy",
        "keywords_tr": ["ileri exergy", "önlenebilir", "onlenebilir", "kaçınılmaz", "endojen", "eksojen", "ayrıştırma"],
        "keywords_en": ["advanced exergy", "avoidable", "unavoidable", "endogenous", "exogenous", "splitting"],
        "files_equipment": lambda eq: [],
        "files_factory": lambda: _glob_knowledge("factory/advanced_exergy"),
    },
    {
        "topic": "thermoeconomic",
        "keywords_tr": ["termoekonomik", "optimizasyon", "çok amaçlı", "pareto"],
        "keywords_en": ["thermoeconomic", "optimization", "multi-objective", "pareto"],
        "files_equipment": lambda eq: [],
        "files_factory": lambda: _glob_knowledge("factory/thermoeconomic_optimization"),
    },
    {
        "topic": "exergoeconomic",
        "keywords_tr": ["exergoekonomik", "speco", "maliyet akışı", "exerji maliyeti"],
        "keywords_en": ["exergoeconomic", "speco", "cost flow", "exergy cost"],
        "files_equipment": lambda eq: [],
        "files_factory": lambda: _glob_knowledge("factory/exergoeconomic"),
    },
    {
        "topic": "energy_management",
        "keywords_tr": ["iso 50001", "enerji yönetimi", "enerji yonetimi", "enpi", "izleme"],
        "keywords_en": ["iso 50001", "energy management", "enpi", "monitoring"],
        "files_equipment": lambda eq: [],
        "files_factory": lambda: _glob_knowledge("factory/energy_management"),
    },
    {
        "topic": "equipment_detail",
        "keywords_tr": ["nasıl çalışır", "nasil calisir", "çalışma prensibi", "tip", "seçim", "secim"],
        "keywords_en": ["how it works", "principle", "type", "selection"],
        "files_equipment": lambda eq: _glob_knowledge(f"{eq}/equipment"),
        "files_factory": [],
    },
    {
        "topic": "benchmark",
        "keywords_tr": ["benchmark", "karşılaştırma", "karsilastirma", "sektör", "sektor", "referans"],
        "keywords_en": ["benchmark", "comparison", "sector", "reference", "best practice"],
        "files_equipment": lambda eq: [f"knowledge/{eq}/benchmarks.md"],
        "files_factory": ["knowledge/factory/factory_benchmarks.md"],
    },
    {
        "topic": "heat_recovery",
        "keywords_tr": ["ısı geri kazanım", "isi geri kazanim", "atık ısı", "atik isi", "kojenerasyon", "chp"],
        "keywords_en": ["heat recovery", "waste heat", "cogeneration", "chp"],
        "files_equipment": lambda eq: [f"knowledge/{eq}/solutions/heat_recovery.md"],
        "files_factory": [
            "knowledge/factory/waste_heat_recovery.md",
            "knowledge/factory/cogeneration.md",
            "knowledge/factory/heat_integration.md",
        ],
    },
]

# ---------------------------------------------------------------------------
# Sector mapping — Turkish/English sector names → knowledge file
# ---------------------------------------------------------------------------

SECTOR_MAP = {
    "gıda": "knowledge/factory/sector_food.md",
    "gida": "knowledge/factory/sector_food.md",
    "food": "knowledge/factory/sector_food.md",
    "tekstil": "knowledge/factory/sector_textile.md",
    "textile": "knowledge/factory/sector_textile.md",
    "çimento": "knowledge/factory/sector_cement.md",
    "cimento": "knowledge/factory/sector_cement.md",
    "cement": "knowledge/factory/sector_cement.md",
    "kimya": "knowledge/factory/sector_chemical.md",
    "chemical": "knowledge/factory/sector_chemical.md",
    "kağıt": "knowledge/factory/sector_paper.md",
    "kagit": "knowledge/factory/sector_paper.md",
    "paper": "knowledge/factory/sector_paper.md",
    "metal": "knowledge/factory/sector_metal.md",
    "otomotiv": "knowledge/factory/sector_automotive.md",
    "automotive": "knowledge/factory/sector_automotive.md",
}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def route_knowledge(
    question: str,
    equipment_type: str,
    subtype: Optional[str] = None,
) -> List[str]:
    """Route a user question to the most relevant knowledge files.

    Three tiers:
    - Tier 1 (always): INDEX.md, benchmarks.md, formulas.md for the equipment
    - Tier 2 (keyword match): topic-specific files
    - Tier 3 (fallback): solutions/ files if no topic matched

    Args:
        question: User's question text.
        equipment_type: Equipment type (e.g. 'compressor', 'pump').
        subtype: Optional equipment subtype.

    Returns:
        List of file paths (relative to project root), max 8, deduplicated,
        only files that exist on disk.
    """
    files: List[str] = []

    # Tier 1: Base files for the equipment type
    base_files = [
        f"knowledge/{equipment_type}/INDEX.md",
        f"knowledge/{equipment_type}/benchmarks.md",
        f"knowledge/{equipment_type}/formulas.md",
    ]
    files.extend(base_files)

    # Tier 2: Keyword-matched topics
    question_lower = question.lower()
    topic_matched = False

    for route in TOPIC_ROUTES:
        all_keywords = route["keywords_tr"] + route["keywords_en"]
        if any(kw.lower() in question_lower for kw in all_keywords):
            topic_matched = True

            # Equipment-specific files
            eq_files = route["files_equipment"]
            if callable(eq_files):
                eq_files = eq_files(equipment_type)
            files.extend(eq_files)

            # Factory-level files
            fac_files = route["files_factory"]
            if callable(fac_files):
                fac_files = fac_files()
            files.extend(fac_files)

    # Sector files
    sector_files = _match_sector_files(question)
    files.extend(sector_files)

    # Tier 3: Fallback — load solutions if no topic matched
    if not topic_matched:
        fallback = _glob_knowledge(f"{equipment_type}/solutions")
        files.extend(fallback)

    # Deduplicate while preserving order
    seen: set[str] = set()
    unique: List[str] = []
    for f in files:
        if f not in seen:
            seen.add(f)
            unique.append(f)

    # Filter to files that exist on disk
    existing = [f for f in unique if os.path.isfile(_PROJECT_ROOT / f)]

    # Cap at 8 files
    result = existing[:8]

    logger.debug(
        "route_knowledge(%r, %s) -> %d files: %s",
        question[:50],
        equipment_type,
        len(result),
        [f.split("/")[-1] for f in result],
    )
    return result


def get_knowledge_summary(files: List[str]) -> str:
    """Return a debug/log-friendly summary of routed knowledge files.

    Args:
        files: List of file paths from route_knowledge().

    Returns:
        Human-readable summary string.
    """
    if not files:
        return "No knowledge files routed."
    names = [f.split("/")[-1] for f in files]
    return f"{len(files)} files: {', '.join(names)}"
