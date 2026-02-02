"""Claude Code CLI integration service for AI-powered exergy interpretation."""

import asyncio
import json
import logging
import re
from functools import lru_cache
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

EQUIPMENT_LABELS = {
    "compressor": "Kompresör",
    "boiler": "Kazan",
    "chiller": "Chiller",
    "pump": "Pompa",
}

EQUIPMENT_PARAMS_TEMPLATE = {
    "compressor": """- Güç: {power_kW} kW
- Debi: {flow_rate_m3_min} m³/min
- Çıkış Basıncı: {outlet_pressure_bar} bar
- Çalışma Saati: {operating_hours} saat/yıl
- Yük Faktörü: {load_factor}
- Elektrik Fiyatı: {electricity_price_eur_kwh} €/kWh""",
    "boiler": """- Yakıt Debisi: {fuel_flow_kg_h} kg/h
- Buhar/Su Debisi: {steam_flow_kg_h} kg/h
- Buhar Basıncı: {steam_pressure_bar} bar
- Besleme Suyu Sıcaklığı: {feedwater_temp_C} °C
- Baca Gazı Sıcaklığı: {flue_gas_temp_C} °C
- Yakıt Tipi: {fuel_type}
- Fazla Hava: {excess_air_pct}%
- Çalışma Saati: {operating_hours} saat/yıl
- Yakıt Fiyatı: {fuel_price_eur_kg} €/kg""",
    "chiller": """- Soğutma Kapasitesi: {cooling_capacity_kW} kW
- Kompresör Gücü: {compressor_power_kW} kW
- Soğuk Su Çıkış: {chw_supply_temp_C} °C
- Soğuk Su Dönüş: {chw_return_temp_C} °C
- Kondenser Su Giriş: {cw_supply_temp_C} °C
- Kondenser Su Çıkış: {cw_return_temp_C} °C
- Çalışma Saati: {operating_hours} saat/yıl
- Elektrik Fiyatı: {electricity_price_eur_kwh} €/kWh""",
    "pump": """- Motor Gücü: {motor_power_kW} kW
- Debi: {flow_rate_m3_h} m³/h
- Basma Yüksekliği: {total_head_m} m
- Pompa Verimi: {pump_efficiency_pct}%
- Kontrol Yöntemi: {control_method}
- Çalışma Saati: {operating_hours} saat/yıl
- Elektrik Fiyatı: {electricity_price_eur_kwh} €/kWh""",
}

EQUIPMENT_CATEGORIES = {
    "compressor": "heat_recovery|vsd|pressure|maintenance|leaks|system_design|inlet|dryer",
    "boiler": "economizer|air_preheater|oxygen_control|blowdown|condensate|steam_trap|insulation|load_optimization|combustion|feedwater",
    "chiller": "vsd|condenser|chilled_water_reset|free_cooling|sequencing|maintenance|load_reduction|delta_t|thermal_storage|heat_recovery",
    "pump": "vsd|impeller_trimming|right_sizing|parallel|system_optimization|motor_upgrade|maintenance|throttle_elimination|cavitation|control",
}


class _SafeDict(dict):
    """Dict subclass that returns 'N/A' for missing keys in str.format_map()."""

    def __missing__(self, key: str) -> str:
        return "N/A"


@lru_cache(maxsize=100)
def _read_file_cached(file_path: str) -> Optional[str]:
    """Read a file with LRU caching. Returns None if file not found."""
    try:
        return Path(file_path).read_text(encoding="utf-8")
    except FileNotFoundError:
        logger.debug("File not found: %s", file_path)
        return None
    except Exception:
        logger.warning("Error reading file: %s", file_path, exc_info=True)
        return None


class ClaudeCodeClient:
    """Singleton client for Claude Code CLI interactions with modular skill loading."""

    _instance: "ClaudeCodeClient | None" = None

    def __init__(self) -> None:
        self._project_root = Path(__file__).resolve().parent.parent.parent
        self._timeout = 120
        self._skills_dir = self._project_root / "skills"
        self._knowledge_dir = self._project_root / "knowledge"
        # Backwards-compatible: also load legacy SKILL file
        self._skill_content = self._load_skill_file()

    @classmethod
    def get_instance(cls) -> "ClaudeCodeClient":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _load_skill_file(self) -> str:
        """Load the legacy SKILL file content at startup (backwards compatible)."""
        skill_path = self._project_root / "skills" / "SKILL_exergy_interpreter.md"
        try:
            return skill_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            logger.warning("Legacy SKILL file not found at %s", skill_path)
            return ""

    def _load_skill(self, skill_path: str) -> Optional[str]:
        """Load a single modular skill file with caching.

        Args:
            skill_path: Relative path within skills/ directory (e.g. 'core/exergy_fundamentals.md')
        """
        full_path = str(self._skills_dir / skill_path)
        return _read_file_cached(full_path)

    def _load_skills(self, analysis_type: str, equipment_type: Optional[str] = None) -> str:
        """Load relevant skill files based on analysis type and equipment.

        Loading order:
        1. Core skills (always loaded)
        2. Equipment-specific skill (for single equipment analysis)
        3. Factory skills (for factory analysis)
        4. Output skills (always loaded)

        Args:
            analysis_type: 'single_equipment' or 'factory'
            equipment_type: Equipment type for equipment-specific skills
        """
        skills: list[str] = []

        # Core skills — always loaded
        for core_skill in [
            "core/exergy_fundamentals.md",
            "core/response_format.md",
            "core/decision_trees.md",
        ]:
            content = self._load_skill(core_skill)
            if content:
                skills.append(content)

        # Equipment-specific skill
        if equipment_type and equipment_type in EQUIPMENT_LABELS:
            content = self._load_skill(f"equipment/{equipment_type}_expert.md")
            if content:
                skills.append(content)

        # Factory skills
        if analysis_type == "factory":
            for factory_skill in [
                "factory/factory_analyst.md",
                "factory/integration_expert.md",
                "factory/economic_advisor.md",
            ]:
                content = self._load_skill(factory_skill)
                if content:
                    skills.append(content)

        # Output skills — always loaded
        content = self._load_skill("output/turkish_style.md")
        if content:
            skills.append(content)

        return "\n\n---\n\n".join(skills)

    def _load_knowledge_file(self, file_path: str) -> Optional[str]:
        """Load a single knowledge file with caching.

        Args:
            file_path: Relative path from project root (e.g. 'knowledge/compressor/benchmarks.md')
        """
        full_path = str(self._project_root / file_path)
        return _read_file_cached(full_path)

    def _load_relevant_knowledge(
        self,
        analysis_type: str,
        equipment_type: Optional[str] = None,
        sector: Optional[str] = None,
    ) -> str:
        """Load knowledge files relevant to the current analysis context.

        Args:
            analysis_type: 'single_equipment' or 'factory'
            equipment_type: Equipment type for targeted knowledge loading
            sector: Factory sector for sector-specific knowledge
        """
        files: list[str] = []

        if equipment_type and equipment_type in EQUIPMENT_LABELS:
            files.append(f"knowledge/{equipment_type}/benchmarks.md")
            files.append(f"knowledge/{equipment_type}/formulas.md")

        if analysis_type == "factory":
            files.extend([
                "knowledge/factory/cross_equipment.md",
                "knowledge/factory/prioritization.md",
                "knowledge/factory/factory_benchmarks.md",
                "knowledge/factory/exergoeconomic/evaluation_criteria.md",
            ])
            if sector:
                files.append(f"knowledge/factory/sector_{sector}.md")

        contents: list[str] = []
        for f in files:
            content = self._load_knowledge_file(f)
            if content:
                contents.append(f"## {f}\n\n{content}")

        return "\n\n---\n\n".join(contents)

    def _build_prompt(
        self,
        analysis_result: dict,
        equipment_type: str,
        subtype: str,
        parameters: dict,
    ) -> str:
        """Build the prompt sent to Claude Code CLI using modular skills."""
        metrics = analysis_result.get("metrics", {})
        benchmark = analysis_result.get("benchmark", {})
        heat_recovery = analysis_result.get("heat_recovery", {})

        # Handle dual field names from frontend
        efficiency = metrics.get("exergy_efficiency_percent") or metrics.get(
            "exergy_efficiency_pct"
        )

        equipment_label = EQUIPMENT_LABELS.get(equipment_type, equipment_type)
        categories = EQUIPMENT_CATEGORIES.get(equipment_type, "")

        # Load modular skills for this analysis
        skills_content = self._load_skills("single_equipment", equipment_type)

        # Load relevant knowledge files
        knowledge_content = self._load_relevant_knowledge(
            "single_equipment", equipment_type
        )

        # Fall back to legacy SKILL file if modular skills are empty
        if not skills_content:
            skills_content = self._skill_content

        # Build parameters section with safe formatting (missing keys → 'N/A')
        params_template = EQUIPMENT_PARAMS_TEMPLATE.get(equipment_type, "")
        safe_params = {k: v for k, v in parameters.items()}
        try:
            params_section = params_template.format_map(
                _SafeDict(safe_params)
            )
        except Exception:
            params_section = str(parameters)

        # Build knowledge section
        knowledge_section = ""
        if knowledge_content:
            knowledge_section = f"""

## Bilgi Kaynakları (Knowledge Base)

{knowledge_content}
"""

        return f"""Sen bir endüstriyel exergy analizi uzmanısın. Aşağıdaki {equipment_label.lower()} analiz sonuçlarını yorumla.

## Yorumlama Kuralları ve Şema

{skills_content}
{knowledge_section}
## Analiz Verileri

**Ekipman Tipi:** {equipment_label}
**Alt Tip:** {subtype}

**Parametreler:**
{params_section}

**Exergy Metrikleri:**
- Exergy Girişi: {metrics.get('exergy_input_kW', 'N/A')} kW
- Faydalı Exergy: {metrics.get('exergy_output_kW', 'N/A')} kW
- Exergy Yıkımı: {metrics.get('exergy_destroyed_kW', 'N/A')} kW
- Exergy Verimi: {efficiency}%
- Yıllık Kayıp: {metrics.get('annual_loss_kWh', 'N/A')} kWh
- Yıllık Maliyet: {metrics.get('annual_cost_eur', 'N/A')} €

**Isı Geri Kazanım:**
- Potansiyel: {heat_recovery.get('potential_kW', 'N/A')} kW
- Yıllık Tasarruf: {heat_recovery.get('annual_savings_eur', 'N/A')} €/yıl

**Benchmark:**
- Değerlendirme: {benchmark.get('rating', 'N/A')}
- Yüzdelik: {benchmark.get('percentile', 'N/A')}

## Görev

Yukarıdaki verileri analiz et ve SKILL dosyasındaki JSON şemasına uygun yanıt ver. Markdown fence kullanma, saf JSON döndür.

{{
  "summary": "2-3 cümlelik genel özet",
  "detailed_analysis": "Detaylı exergy analizi açıklaması (3-5 cümle)",
  "key_insights": ["Bulgu 1", "Bulgu 2", "Bulgu 3"],
  "recommendations": [
    {{
      "title": "Öneri başlığı",
      "description": "Detaylı açıklama",
      "priority": "high|medium|low",
      "estimated_savings_eur_year": 5000,
      "estimated_investment_eur": 15000,
      "payback_years": 3.0,
      "category": "{categories}"
    }}
  ],
  "not_recommended": [
    {{
      "title": "Önerilmeyen çözüm",
      "reason": "Neden uygun olmadığı"
    }}
  ],
  "action_plan": {{
    "immediate": ["Hemen yapılabilecek aksiyonlar"],
    "short_term": ["1-3 ay içinde"],
    "medium_term": ["3-12 ay içinde"]
  }},
  "warnings": ["Uyarılar"]
}}"""

    @staticmethod
    def _extract_json(text: str) -> dict | None:
        """3-tier JSON parser: direct → markdown fence → regex extraction."""
        # Tier 1: Try parsing entire output as JSON
        try:
            return json.loads(text)
        except (json.JSONDecodeError, TypeError):
            pass

        # Tier 2: Extract from markdown fences
        match = re.search(r"```(?:json)?\s*\n?(.*?)\n?\s*```", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1).strip())
            except json.JSONDecodeError:
                pass

        # Tier 3: Find raw JSON object via regex
        match = re.search(r"\{[\s\S]*\}", text)
        if match:
            try:
                return json.loads(match.group(0).strip())
            except json.JSONDecodeError:
                pass

        return None

    @staticmethod
    def _fallback_response() -> dict:
        """Return a fallback response when AI is unavailable."""
        return {
            "ai_available": False,
            "summary": "",
            "detailed_analysis": "",
            "key_insights": [],
            "recommendations": [],
            "not_recommended": [],
            "action_plan": {"immediate": [], "short_term": [], "medium_term": []},
            "warnings": [],
        }

    async def interpret(
        self,
        analysis_result: dict,
        equipment_type: str,
        subtype: str,
        parameters: dict,
    ) -> dict:
        """Run Claude Code CLI to interpret exergy analysis results.

        Returns a dict with ai_available=True and interpretation data on success,
        or ai_available=False with empty fields on failure.
        """
        prompt = self._build_prompt(analysis_result, equipment_type, subtype, parameters)

        try:
            logger.info("Claude Code CLI called")
            process = await asyncio.create_subprocess_exec(
                "claude",
                "-p",
                prompt,
                cwd=str(self._project_root),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, stderr = await asyncio.wait_for(
                process.communicate(), timeout=self._timeout
            )

            if process.returncode != 0:
                logger.warning(
                    "Claude CLI exited with code %d: %s",
                    process.returncode,
                    stderr.decode(errors="replace")[:500],
                )
                return self._fallback_response()

            raw_output = stdout.decode(errors="replace")
            logger.info("Claude Code response received, parsing")

            # Single-layer parsing — no JSON envelope with -p flag
            interpretation = self._extract_json(raw_output)
            if interpretation is None:
                logger.warning("Could not extract JSON from Claude response")
                return self._fallback_response()

            interpretation["ai_available"] = True
            return interpretation

        except asyncio.TimeoutError:
            logger.warning("Claude CLI timed out after %ds", self._timeout)
            return self._fallback_response()
        except FileNotFoundError:
            logger.warning("Claude CLI not found in PATH")
            return self._fallback_response()
        except Exception:
            logger.exception("Unexpected error calling Claude CLI")
            return self._fallback_response()


async def interpret_with_claude_code(
    analysis_result: dict,
    equipment_type: str,
    subtype: str,
    parameters: dict,
) -> dict:
    """Module-level function preserving the existing import interface.

    Delegates to the ClaudeCodeClient singleton.
    """
    client = ClaudeCodeClient.get_instance()
    return await client.interpret(analysis_result, equipment_type, subtype, parameters)


def _format_factory_analysis(project: dict) -> str:
    """Format factory analysis data for AI prompt."""
    lines = []
    lines.append(f"**Fabrika Adi:** {project.get('name', 'N/A')}")
    lines.append(f"**Sektor:** {project.get('sector', 'N/A')}")
    lines.append(f"**Ekipman Sayisi:** {len(project.get('equipment', []))}")
    lines.append("")

    for eq in project.get("equipment", []):
        result = eq.get("analysis_result")
        if not result:
            continue
        lines.append(f"### {eq.get('name', 'N/A')} ({eq.get('type', '')}/{eq.get('subtype', '')})")
        lines.append(f"- Exergy Girisi: {result.get('exergy_in_kW', 'N/A')} kW")
        lines.append(f"- Exergy Cikisi: {result.get('exergy_out_kW', 'N/A')} kW")
        lines.append(f"- Exergy Yikimi: {result.get('exergy_destroyed_kW', 'N/A')} kW")
        lines.append(f"- Exergy Verimi: {result.get('exergy_efficiency_pct', 'N/A')}%")
        annual_loss = result.get('annual_loss_EUR', 'N/A')
        lines.append(f"- Yillik Kayip: {annual_loss} EUR")
        lines.append("")

    return "\n".join(lines)


def _fallback_factory_response() -> dict:
    """Return a fallback response for factory interpretation."""
    return {
        "ai_available": False,
        "summary": "",
        "hotspot_analysis": [],
        "integration_opportunities": [],
        "prioritized_actions": [],
        "sector_specific_insights": [],
        "warnings": [],
    }


async def interpret_factory_analysis(
    project: dict,
    sector: str | None = None,
) -> dict:
    """Run Claude Code CLI to interpret factory-level analysis results."""
    client = ClaudeCodeClient.get_instance()

    analysis_summary = _format_factory_analysis(project)

    sector_label = sector or project.get("sector") or "genel"

    # Load modular factory skills and knowledge
    skills_content = client._load_skills("factory")
    knowledge_content = client._load_relevant_knowledge("factory", sector=sector_label)

    # Build knowledge section
    knowledge_section = ""
    if knowledge_content:
        knowledge_section = f"""

## Bilgi Kaynaklari (Knowledge Base)

{knowledge_content}
"""

    # Build skills section (fall back to inline references if modular skills empty)
    if not skills_content:
        skills_section = """## Bilgi Kaynaklari

Fabrika yorumlamasi icin asagidaki knowledge dosyalarini referans al:
- knowledge/factory/cross_equipment.md — Capraz ekipman entegrasyon firsatlari
- knowledge/factory/prioritization.md — Yatirim onceliklendirme
- knowledge/factory/factory_benchmarks.md — Fabrika benchmark verileri"""
    else:
        skills_section = f"""## Yorumlama Kurallari ve Skill'ler

{skills_content}"""

    prompt = f"""Sen bir endustriyel exergy analizi uzmanisin. Asagidaki fabrika seviyesi analiz sonuclarini yorumla.

{skills_section}
{knowledge_section}
## Fabrika Verileri

{analysis_summary}

**Sektor:** {sector_label}

## Gorev

Fabrika genelindeki exergy kayiplarini, hotspot'lari, capraz ekipman entegrasyon firsatlarini ve oncelikli aksiyonlari analiz et.
Sektore ozel bulgulari belirt. Asagidaki JSON semasina uygun yanit ver. Markdown fence kullanma, saf JSON dondur.

{{
  "summary": "Fabrika geneli 2-3 cumlelik ozet",
  "hotspot_analysis": [
    {{
      "equipment_name": "Ekipman adi",
      "equipment_type": "compressor|boiler|chiller|pump",
      "exergy_destroyed_kW": 15.5,
      "priority": "high|medium|low",
      "finding": "Bulgu aciklamasi"
    }}
  ],
  "integration_opportunities": [
    {{
      "title": "Entegrasyon firsati",
      "source": "Kaynak ekipman",
      "target": "Hedef ekipman/proses",
      "potential_savings_eur_year": 5000,
      "complexity": "low|medium|high",
      "description": "Detayli aciklama"
    }}
  ],
  "prioritized_actions": [
    {{
      "rank": 1,
      "action": "Aksiyon aciklamasi",
      "estimated_savings_eur_year": 10000,
      "estimated_investment_eur": 15000,
      "payback_years": 1.5,
      "priority": "high|medium|low"
    }}
  ],
  "sector_specific_insights": ["Sektore ozel bulgu 1", "Bulgu 2"],
  "warnings": ["Uyari 1"]
}}"""

    try:
        logger.info("Claude Code CLI called for factory interpretation")
        process = await asyncio.create_subprocess_exec(
            "claude",
            "-p",
            prompt,
            cwd=str(client._project_root),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout, stderr = await asyncio.wait_for(
            process.communicate(), timeout=client._timeout
        )

        if process.returncode != 0:
            logger.warning(
                "Claude CLI exited with code %d: %s",
                process.returncode,
                stderr.decode(errors="replace")[:500],
            )
            return _fallback_factory_response()

        raw_output = stdout.decode(errors="replace")
        logger.info("Claude Code factory response received, parsing")

        interpretation = client._extract_json(raw_output)
        if interpretation is None:
            logger.warning("Could not extract JSON from Claude factory response")
            return _fallback_factory_response()

        interpretation["ai_available"] = True
        return interpretation

    except asyncio.TimeoutError:
        logger.warning("Claude CLI timed out for factory interpretation")
        return _fallback_factory_response()
    except FileNotFoundError:
        logger.warning("Claude CLI not found in PATH")
        return _fallback_factory_response()
    except Exception:
        logger.exception("Unexpected error in factory interpretation")
        return _fallback_factory_response()
