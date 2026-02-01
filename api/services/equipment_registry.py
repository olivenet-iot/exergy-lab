"""Equipment type registry for ExergyLab."""

EQUIPMENT_TYPES = {
    "compressor": {
        "id": "compressor",
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
        "engine_ready": True,
    },
    "boiler": {
        "id": "boiler",
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
        "engine_ready": False,
    },
    "chiller": {
        "id": "chiller",
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
        "engine_ready": False,
    },
    "pump": {
        "id": "pump",
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
        "engine_ready": False,
    },
}


def get_equipment_types():
    """Return all equipment types for frontend."""
    return [
        {
            "id": eq_id,
            "name": eq_data["name"],
            "name_en": eq_data["name_en"],
            "icon": eq_data["icon"],
            "subtypes": eq_data["subtypes"],
            "engine_ready": eq_data["engine_ready"],
        }
        for eq_id, eq_data in EQUIPMENT_TYPES.items()
    ]


def get_equipment_subtypes(equipment_type: str):
    """Return subtypes for a given equipment type."""
    if equipment_type not in EQUIPMENT_TYPES:
        return []
    return EQUIPMENT_TYPES[equipment_type]["subtypes"]


def get_knowledge_path(equipment_type: str) -> str:
    """Return knowledge base path for an equipment type."""
    if equipment_type not in EQUIPMENT_TYPES:
        return "knowledge"
    return EQUIPMENT_TYPES[equipment_type]["knowledge_path"]


def is_valid_equipment(equipment_type: str, subtype: str = None) -> bool:
    """Check if equipment type (and optional subtype) is valid."""
    if equipment_type not in EQUIPMENT_TYPES:
        return False
    if subtype:
        valid_subtypes = [s["id"] for s in EQUIPMENT_TYPES[equipment_type]["subtypes"]]
        return subtype in valid_subtypes
    return True


def is_engine_ready(equipment_type: str) -> bool:
    """Check if the analysis engine is implemented for this equipment type."""
    if equipment_type not in EQUIPMENT_TYPES:
        return False
    return EQUIPMENT_TYPES[equipment_type]["engine_ready"]
