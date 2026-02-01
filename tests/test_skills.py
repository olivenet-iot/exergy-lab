"""Tests for the modular skill system and ClaudeCodeClient skill loading."""

import os
from pathlib import Path

import pytest

from api.services.claude_code_service import ClaudeCodeClient, _read_file_cached

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def clear_caches():
    """Clear LRU caches between tests so file reads are fresh."""
    _read_file_cached.cache_clear()
    # Reset singleton so each test gets a fresh client
    ClaudeCodeClient._instance = None
    yield
    ClaudeCodeClient._instance = None
    _read_file_cached.cache_clear()


@pytest.fixture
def client():
    """Return a fresh ClaudeCodeClient instance."""
    return ClaudeCodeClient()


# ---------------------------------------------------------------------------
# Skill file existence tests
# ---------------------------------------------------------------------------

class TestSkillFileExistence:
    """Verify all expected skill files exist on disk."""

    CORE_SKILLS = [
        "core/exergy_fundamentals.md",
        "core/response_format.md",
        "core/decision_trees.md",
    ]

    EQUIPMENT_SKILLS = [
        "equipment/compressor_expert.md",
        "equipment/boiler_expert.md",
        "equipment/chiller_expert.md",
        "equipment/pump_expert.md",
    ]

    FACTORY_SKILLS = [
        "factory/factory_analyst.md",
        "factory/integration_expert.md",
    ]

    OUTPUT_SKILLS = [
        "output/turkish_style.md",
    ]

    ALL_SKILLS = CORE_SKILLS + EQUIPMENT_SKILLS + FACTORY_SKILLS + OUTPUT_SKILLS

    @pytest.mark.parametrize("skill_path", ALL_SKILLS)
    def test_skill_file_exists(self, skill_path):
        """Each skill file should exist on disk."""
        full_path = SKILLS_DIR / skill_path
        assert full_path.exists(), f"Skill file missing: {full_path}"

    def test_skills_readme_exists(self):
        """skills/README.md should exist."""
        assert (SKILLS_DIR / "README.md").exists()

    def test_legacy_skill_files_still_exist(self):
        """Legacy SKILL files should still be present for backwards compatibility."""
        assert (SKILLS_DIR / "SKILL_exergy_interpreter.md").exists()
        assert (SKILLS_DIR / "SKILL_exergy_calculator.md").exists()


# ---------------------------------------------------------------------------
# Skill content validation tests
# ---------------------------------------------------------------------------

class TestSkillContentValidation:
    """Validate that skill files have required structural elements."""

    @pytest.mark.parametrize("skill_path", TestSkillFileExistence.ALL_SKILLS)
    def test_skill_has_yaml_frontmatter(self, skill_path):
        """Each skill should start with YAML frontmatter (---)."""
        content = (SKILLS_DIR / skill_path).read_text(encoding="utf-8")
        assert content.startswith("---"), f"{skill_path} missing YAML frontmatter"
        # Should have closing ---
        second_delim = content.index("---", 3)
        assert second_delim > 3, f"{skill_path} has incomplete YAML frontmatter"

    @pytest.mark.parametrize("skill_path", TestSkillFileExistence.ALL_SKILLS)
    def test_skill_has_skill_id(self, skill_path):
        """Each skill should declare a skill_id in frontmatter."""
        content = (SKILLS_DIR / skill_path).read_text(encoding="utf-8")
        assert "skill_id:" in content, f"{skill_path} missing skill_id"

    @pytest.mark.parametrize("skill_path", TestSkillFileExistence.ALL_SKILLS)
    def test_skill_has_version(self, skill_path):
        """Each skill should declare a version in frontmatter."""
        content = (SKILLS_DIR / skill_path).read_text(encoding="utf-8")
        assert "version:" in content, f"{skill_path} missing version"

    @pytest.mark.parametrize("skill_path", TestSkillFileExistence.ALL_SKILLS)
    def test_skill_has_heading(self, skill_path):
        """Each skill should have at least one markdown heading."""
        content = (SKILLS_DIR / skill_path).read_text(encoding="utf-8")
        assert "\n# " in content, f"{skill_path} missing top-level heading"

    def test_compressor_expert_content(self):
        """Compressor expert should contain key domain terms."""
        content = (SKILLS_DIR / "equipment/compressor_expert.md").read_text(encoding="utf-8")
        assert "Kompresör Uzmanı" in content
        assert "Spesifik güç" in content or "spesifik güç" in content
        assert "VSD" in content

    def test_boiler_expert_content(self):
        """Boiler expert should contain key domain terms."""
        content = (SKILLS_DIR / "equipment/boiler_expert.md").read_text(encoding="utf-8")
        assert "Kazan Uzmanı" in content
        assert "Ekonomizer" in content or "ekonomizer" in content

    def test_chiller_expert_content(self):
        """Chiller expert should contain key domain terms."""
        content = (SKILLS_DIR / "equipment/chiller_expert.md").read_text(encoding="utf-8")
        assert "Chiller Uzmanı" in content
        assert "COP" in content

    def test_pump_expert_content(self):
        """Pump expert should contain key domain terms."""
        content = (SKILLS_DIR / "equipment/pump_expert.md").read_text(encoding="utf-8")
        assert "Pompa Uzmanı" in content
        assert "Wire-to-water" in content or "wire-to-water" in content

    def test_decision_trees_has_all_equipment(self):
        """Decision trees should cover all four equipment types."""
        content = (SKILLS_DIR / "core/decision_trees.md").read_text(encoding="utf-8")
        assert "Kompresör" in content
        assert "Kazan" in content
        assert "Chiller" in content or "chiller" in content
        assert "Pompa" in content

    def test_response_format_has_json_schemas(self):
        """Response format should contain JSON schema examples."""
        content = (SKILLS_DIR / "core/response_format.md").read_text(encoding="utf-8")
        assert '"summary"' in content
        assert '"recommendations"' in content
        assert '"hotspot_analysis"' in content


# ---------------------------------------------------------------------------
# Client skill loading tests
# ---------------------------------------------------------------------------

class TestSkillLoading:
    """Test ClaudeCodeClient._load_skills() method."""

    def test_load_single_skill(self, client):
        """Loading a single skill file should return its content."""
        content = client._load_skill("core/exergy_fundamentals.md")
        assert content is not None
        assert "Exergy Temelleri" in content

    def test_load_nonexistent_skill(self, client):
        """Loading a missing skill should return None, not raise."""
        content = client._load_skill("nonexistent/missing.md")
        assert content is None

    def test_load_skills_single_equipment_compressor(self, client):
        """Single equipment (compressor) should load core + compressor + output skills."""
        combined = client._load_skills("single_equipment", "compressor")
        assert "Exergy Temelleri" in combined       # core/exergy_fundamentals
        assert "Kompresör Uzmanı" in combined       # equipment/compressor_expert
        assert "Türkçe Yazım" in combined           # output/turkish_style
        # Should NOT contain factory skills
        assert "Fabrika Analisti" not in combined

    def test_load_skills_single_equipment_boiler(self, client):
        """Single equipment (boiler) should load core + boiler + output skills."""
        combined = client._load_skills("single_equipment", "boiler")
        assert "Kazan Uzmanı" in combined
        assert "Kompresör Uzmanı" not in combined   # should not cross-load

    def test_load_skills_single_equipment_chiller(self, client):
        """Single equipment (chiller) should load core + chiller + output skills."""
        combined = client._load_skills("single_equipment", "chiller")
        assert "Chiller Uzmanı" in combined

    def test_load_skills_single_equipment_pump(self, client):
        """Single equipment (pump) should load core + pump + output skills."""
        combined = client._load_skills("single_equipment", "pump")
        assert "Pompa Uzmanı" in combined

    def test_load_skills_factory(self, client):
        """Factory analysis should load core + factory + output skills."""
        combined = client._load_skills("factory")
        assert "Exergy Temelleri" in combined       # core
        assert "Fabrika Analisti" in combined        # factory/factory_analyst
        assert "Entegrasyon Uzmanı" in combined     # factory/integration_expert
        assert "Türkçe Yazım" in combined           # output/turkish_style

    def test_load_skills_unknown_equipment(self, client):
        """Unknown equipment type should still load core + output skills."""
        combined = client._load_skills("single_equipment", "unknown_type")
        assert "Exergy Temelleri" in combined
        assert "Türkçe Yazım" in combined

    def test_skills_caching(self, client):
        """Loading the same skill twice should use the cache."""
        content1 = client._load_skill("core/exergy_fundamentals.md")
        content2 = client._load_skill("core/exergy_fundamentals.md")
        assert content1 is content2  # Same object (cached)


# ---------------------------------------------------------------------------
# Knowledge loading tests
# ---------------------------------------------------------------------------

class TestKnowledgeLoading:
    """Test ClaudeCodeClient._load_relevant_knowledge() method."""

    def test_load_knowledge_single_equipment(self, client):
        """Single equipment should load benchmarks + formulas."""
        knowledge = client._load_relevant_knowledge("single_equipment", "compressor")
        assert "compressor/benchmarks.md" in knowledge
        assert "compressor/formulas.md" in knowledge

    def test_load_knowledge_factory(self, client):
        """Factory analysis should load cross-equipment + prioritization + benchmarks."""
        knowledge = client._load_relevant_knowledge("factory")
        assert "factory/cross_equipment.md" in knowledge
        assert "factory/prioritization.md" in knowledge
        assert "factory/factory_benchmarks.md" in knowledge

    def test_load_knowledge_factory_with_sector(self, client):
        """Factory with sector should also load sector file."""
        knowledge = client._load_relevant_knowledge("factory", sector="food")
        assert "factory/sector_food.md" in knowledge

    def test_load_knowledge_missing_sector_file(self, client):
        """Non-existent sector should not break loading."""
        knowledge = client._load_relevant_knowledge("factory", sector="nonexistent")
        # Should still have the core factory files
        assert "factory/cross_equipment.md" in knowledge


# ---------------------------------------------------------------------------
# Knowledge file YAML frontmatter tests
# ---------------------------------------------------------------------------

class TestKnowledgeFrontmatter:
    """Verify knowledge files have YAML frontmatter."""

    EQUIPMENT_TYPES = ["compressor", "boiler", "chiller", "pump"]

    @pytest.mark.parametrize("equipment_type", EQUIPMENT_TYPES)
    def test_benchmarks_has_frontmatter(self, equipment_type):
        """Each equipment benchmarks.md should have YAML frontmatter."""
        path = KNOWLEDGE_DIR / equipment_type / "benchmarks.md"
        content = path.read_text(encoding="utf-8")
        assert content.startswith("---"), f"{path} missing YAML frontmatter"

    @pytest.mark.parametrize("equipment_type", EQUIPMENT_TYPES)
    def test_formulas_has_frontmatter(self, equipment_type):
        """Each equipment formulas.md should have YAML frontmatter."""
        path = KNOWLEDGE_DIR / equipment_type / "formulas.md"
        content = path.read_text(encoding="utf-8")
        assert content.startswith("---"), f"{path} missing YAML frontmatter"

    @pytest.mark.parametrize("equipment_type", EQUIPMENT_TYPES)
    def test_sub_index_exists(self, equipment_type):
        """Each equipment category should have an INDEX.md."""
        path = KNOWLEDGE_DIR / equipment_type / "INDEX.md"
        assert path.exists(), f"Sub-INDEX missing: {path}"

    def test_factory_index_exists(self):
        """Factory should have an INDEX.md."""
        path = KNOWLEDGE_DIR / "factory" / "INDEX.md"
        assert path.exists()

    def test_factory_cross_equipment_has_frontmatter(self):
        """Factory cross_equipment.md should have YAML frontmatter."""
        path = KNOWLEDGE_DIR / "factory" / "cross_equipment.md"
        content = path.read_text(encoding="utf-8")
        assert content.startswith("---")


# ---------------------------------------------------------------------------
# Prompt building tests
# ---------------------------------------------------------------------------

class TestPromptBuilding:
    """Test that _build_prompt integrates skills and knowledge correctly."""

    def test_build_prompt_includes_skills(self, client):
        """Built prompt should contain modular skill content."""
        analysis_result = {
            "metrics": {"exergy_efficiency_percent": 55, "exergy_input_kW": 32},
            "benchmark": {"rating": "average"},
            "heat_recovery": {},
        }
        prompt = client._build_prompt(analysis_result, "compressor", "screw", {"power_kW": 32})
        # Should contain skill content, not just the legacy monolithic file
        assert "Kompresör Uzmanı" in prompt or "Exergy Temelleri" in prompt

    def test_build_prompt_includes_analysis_data(self, client):
        """Built prompt should contain the analysis metrics."""
        analysis_result = {
            "metrics": {"exergy_efficiency_percent": 55, "exergy_input_kW": 32},
            "benchmark": {"rating": "good"},
            "heat_recovery": {"potential_kW": 25},
        }
        prompt = client._build_prompt(analysis_result, "compressor", "screw", {"power_kW": 32})
        assert "55" in prompt  # efficiency value
        assert "Kompresör" in prompt

    def test_build_prompt_safe_dict_handles_missing_params(self, client):
        """Missing parameters should show 'N/A', not raise."""
        analysis_result = {
            "metrics": {},
            "benchmark": {},
            "heat_recovery": {},
        }
        # Pass incomplete parameters — should not raise
        prompt = client._build_prompt(analysis_result, "compressor", "screw", {})
        assert "N/A" in prompt


# ---------------------------------------------------------------------------
# Fallback response tests
# ---------------------------------------------------------------------------

class TestFallbackResponses:
    """Test fallback response structures."""

    def test_equipment_fallback_structure(self):
        """Fallback response should have all expected keys."""
        resp = ClaudeCodeClient._fallback_response()
        assert resp["ai_available"] is False
        assert "summary" in resp
        assert "recommendations" in resp
        assert "action_plan" in resp
        assert isinstance(resp["key_insights"], list)

    def test_factory_fallback_structure(self):
        """Factory fallback should have all expected keys."""
        from api.services.claude_code_service import _fallback_factory_response
        resp = _fallback_factory_response()
        assert resp["ai_available"] is False
        assert "hotspot_analysis" in resp
        assert "integration_opportunities" in resp
        assert "prioritized_actions" in resp


# ---------------------------------------------------------------------------
# JSON extraction tests
# ---------------------------------------------------------------------------

class TestJsonExtraction:
    """Test the _extract_json parser."""

    def test_direct_json(self):
        """Should parse direct JSON string."""
        result = ClaudeCodeClient._extract_json('{"summary": "test"}')
        assert result == {"summary": "test"}

    def test_json_in_markdown_fence(self):
        """Should extract JSON from markdown code fence."""
        text = 'Some text\n```json\n{"summary": "test"}\n```\nMore text'
        result = ClaudeCodeClient._extract_json(text)
        assert result == {"summary": "test"}

    def test_embedded_json(self):
        """Should extract embedded JSON from text."""
        text = 'Preamble text\n{"summary": "test", "key": 123}\nTrailing text'
        result = ClaudeCodeClient._extract_json(text)
        assert result is not None
        assert result["summary"] == "test"

    def test_invalid_json(self):
        """Should return None for invalid JSON."""
        result = ClaudeCodeClient._extract_json("not json at all")
        assert result is None

    def test_empty_input(self):
        """Should return None for empty input."""
        result = ClaudeCodeClient._extract_json("")
        assert result is None
