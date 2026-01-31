"""Claude Code CLI integration service for AI-powered exergy interpretation."""

import asyncio
import json
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

PROJECT_ROOT = str(Path(__file__).resolve().parent.parent.parent)

TIMEOUT_SECONDS = 120


def _extract_json_string(text: str) -> str | None:
    """Extract JSON from text, handling markdown fences and raw JSON."""
    # Try markdown fence first
    match = re.search(r"```(?:json)?\s*\n?(.*?)\n?\s*```", text, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Try to find raw JSON object
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        return match.group(0).strip()

    return None


def _build_interpretation_prompt(
    analysis_result: dict,
    compressor_type: str,
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

    return f"""Sen bir endüstriyel exergy analizi uzmanısın. Aşağıdaki kompresör analiz sonuçlarını yorumla.

Bilgi tabanı dosyalarını referans al:
- /knowledge/benchmarks/compressor_benchmarks.md
- /knowledge/equipment/compressor_{compressor_type}.md
- /knowledge/solutions/ altındaki tüm çözüm dosyaları

## Analiz Verileri

**Kompresör Tipi:** {compressor_type}

**Parametreler:**
- Güç: {parameters.get('power_kW', 'N/A')} kW
- Debi: {parameters.get('flow_rate_m3_min', 'N/A')} m³/min
- Çıkış Basıncı: {parameters.get('outlet_pressure_bar', 'N/A')} bar
- Çalışma Saati: {parameters.get('operating_hours', 4000)} saat/yıl
- Yük Faktörü: {parameters.get('load_factor', 0.75)}
- Elektrik Fiyatı: {parameters.get('electricity_price_eur_kwh', 0.10)} €/kWh

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

Yukarıdaki verileri analiz et ve aşağıdaki JSON formatında yanıt ver. Markdown fence kullanma, saf JSON döndür.

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
      "category": "heat_recovery|vsd|pressure|maintenance|leaks|system_design|inlet|dryer"
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


async def interpret_with_claude_code(
    analysis_result: dict,
    compressor_type: str,
    parameters: dict,
) -> dict:
    """Run Claude Code CLI to interpret exergy analysis results.

    Returns a dict with ai_available=True and interpretation data on success,
    or ai_available=False with empty fields on failure.
    """
    prompt = _build_interpretation_prompt(analysis_result, compressor_type, parameters)

    try:
        process = await asyncio.create_subprocess_exec(
            "claude",
            "-p",
            prompt,
            "--output-format",
            "json",
            cwd=PROJECT_ROOT,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout, stderr = await asyncio.wait_for(
            process.communicate(), timeout=TIMEOUT_SECONDS
        )

        if process.returncode != 0:
            logger.warning(
                "Claude CLI exited with code %d: %s",
                process.returncode,
                stderr.decode(errors="replace")[:500],
            )
            return _fallback_response()

        raw_output = stdout.decode(errors="replace")

        # Layer 1: Parse the outer CLI JSON envelope
        try:
            cli_response = json.loads(raw_output)
        except json.JSONDecodeError:
            logger.warning("Failed to parse CLI JSON envelope")
            return _fallback_response()

        # Extract the inner result text
        inner_text = cli_response.get("result", "")
        if not inner_text:
            logger.warning("CLI response has no 'result' field")
            return _fallback_response()

        # Layer 2: Parse the LLM's JSON from the result text
        json_str = _extract_json_string(inner_text)
        if not json_str:
            logger.warning("Could not extract JSON from LLM result")
            return _fallback_response()

        try:
            interpretation = json.loads(json_str)
        except json.JSONDecodeError:
            logger.warning("Failed to parse LLM JSON output")
            return _fallback_response()

        interpretation["ai_available"] = True
        return interpretation

    except asyncio.TimeoutError:
        logger.warning("Claude CLI timed out after %ds", TIMEOUT_SECONDS)
        return _fallback_response()
    except FileNotFoundError:
        logger.warning("Claude CLI not found in PATH")
        return _fallback_response()
    except Exception:
        logger.exception("Unexpected error calling Claude CLI")
        return _fallback_response()
