"""Claude Code CLI integration service for AI-powered exergy interpretation."""

import asyncio
import json
import logging
import re
from pathlib import Path

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


class ClaudeCodeClient:
    """Singleton client for Claude Code CLI interactions."""

    _instance: "ClaudeCodeClient | None" = None

    def __init__(self) -> None:
        self._project_root = Path(__file__).resolve().parent.parent.parent
        self._timeout = 120
        self._skill_content = self._load_skill_file()

    @classmethod
    def get_instance(cls) -> "ClaudeCodeClient":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _load_skill_file(self) -> str:
        """Load the SKILL file content at startup."""
        skill_path = self._project_root / "skills" / "SKILL_exergy_interpreter.md"
        try:
            return skill_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            logger.warning("SKILL file not found at %s", skill_path)
            return ""

    def _build_prompt(
        self,
        analysis_result: dict,
        equipment_type: str,
        subtype: str,
        parameters: dict,
    ) -> str:
        """Build the prompt sent to Claude Code CLI."""
        metrics = analysis_result.get("metrics", {})
        benchmark = analysis_result.get("benchmark", {})
        heat_recovery = analysis_result.get("heat_recovery", {})

        # Handle dual field names from frontend
        efficiency = metrics.get("exergy_efficiency_percent") or metrics.get(
            "exergy_efficiency_pct"
        )

        equipment_label = EQUIPMENT_LABELS.get(equipment_type, equipment_type)
        categories = EQUIPMENT_CATEGORIES.get(equipment_type, "")

        # Build parameters section with safe formatting (missing keys → 'N/A')
        params_template = EQUIPMENT_PARAMS_TEMPLATE.get(equipment_type, "")
        safe_params = {k: v for k, v in parameters.items()}
        try:
            params_section = params_template.format_map(
                _SafeDict(safe_params)
            )
        except Exception:
            params_section = str(parameters)

        return f"""Sen bir endüstriyel exergy analizi uzmanısın. Aşağıdaki {equipment_label.lower()} analiz sonuçlarını yorumla.

## Yorumlama Kuralları ve Şema

{self._skill_content}

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
