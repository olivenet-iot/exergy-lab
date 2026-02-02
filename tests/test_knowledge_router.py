"""Tests for knowledge router and chat API endpoint."""

import pytest
from fastapi.testclient import TestClient

from api.main import app
from api.services.knowledge_router import route_knowledge, get_knowledge_summary

client = TestClient(app)


class TestRouteKnowledge:
    """Tests for route_knowledge() function."""

    def test_base_files_always_loaded(self):
        """INDEX.md, benchmarks.md, formulas.md should always be present."""
        files = route_knowledge("herhangi bir soru", "compressor")
        names = [f.split("/")[-1] for f in files]
        assert "INDEX.md" in names
        assert "benchmarks.md" in names
        assert "formulas.md" in names

    def test_solutions_routing(self):
        """'iyileştirme' keyword should trigger solutions/ files."""
        files = route_knowledge("Verim iyileştirme önerileri neler?", "pump")
        names = [f.split("/")[-1] for f in files]
        # Should contain at least one solution file
        solution_files = [n for n in names if n not in ("INDEX.md", "benchmarks.md", "formulas.md")]
        assert len(solution_files) > 0

    def test_audit_routing(self):
        """'denetim' keyword should route to audit.md."""
        files = route_knowledge("Enerji denetim nasıl yapılır?", "boiler")
        names = [f.split("/")[-1] for f in files]
        assert "audit.md" in names

    def test_pinch_routing(self):
        """'pinch' keyword should trigger factory/pinch/ files."""
        files = route_knowledge("Pinch analizi nasıl uygulanır?", "heat_exchanger")
        # Should include pinch-related files
        pinch_files = [f for f in files if "pinch" in f]
        assert len(pinch_files) > 0

    def test_economics_routing(self):
        """'yatırım' keyword should trigger economic files."""
        files = route_knowledge("Yatırım geri dönüş süresi nedir?", "compressor")
        # Should include economic-related files
        econ_files = [f for f in files if "economic" in f or "cost" in f or "benchmarks" in f]
        assert len(econ_files) > 0

    def test_entropy_routing(self):
        """'Bejan' keyword should trigger entropy_generation/ files."""
        files = route_knowledge("Bejan sayısı ne anlama gelir?", "compressor")
        entropy_files = [f for f in files if "entropy" in f]
        assert len(entropy_files) > 0

    def test_max_files_limit(self):
        """Multi-keyword query should stay <= 8 files."""
        # Use a question that matches many topics
        files = route_knowledge(
            "Pinch analizi, Bejan sayısı, yatırım maliyeti ve iyileştirme önerileri",
            "compressor",
        )
        assert len(files) <= 8

    def test_no_duplicates(self):
        """All returned files should be unique."""
        files = route_knowledge("benchmark karşılaştırma ve iyileştirme", "pump")
        assert len(files) == len(set(files))

    def test_unknown_equipment(self):
        """Unknown equipment type should return a list (no crash)."""
        files = route_knowledge("test sorusu", "unknown_type")
        assert isinstance(files, list)

    def test_all_equipment_types(self):
        """All 7 equipment types should return at least 1 file."""
        equipment_types = [
            "compressor", "boiler", "chiller", "pump",
            "heat_exchanger", "steam_turbine", "dryer",
        ]
        for eq in equipment_types:
            files = route_knowledge("genel soru", eq)
            assert len(files) >= 1, f"{eq} returned no files"

    def test_sector_routing(self):
        """'gıda' keyword should trigger sector_food.md."""
        files = route_knowledge("Gıda sektöründe exergy analizi", "compressor")
        food_files = [f for f in files if "sector_food" in f]
        assert len(food_files) > 0

    def test_fallback_loads_solutions(self):
        """Unmatched query should fall back to solutions/ files."""
        # Use a question with no topic keywords
        files = route_knowledge("xyz abc 123 bilinmeyen", "compressor")
        # Should include solutions as fallback (beyond base files)
        names = [f.split("/")[-1] for f in files]
        non_base = [n for n in names if n not in ("INDEX.md", "benchmarks.md", "formulas.md")]
        assert len(non_base) > 0


class TestGetKnowledgeSummary:
    """Tests for get_knowledge_summary() helper."""

    def test_empty_files(self):
        result = get_knowledge_summary([])
        assert "No knowledge files" in result

    def test_summary_format(self):
        files = ["knowledge/compressor/INDEX.md", "knowledge/compressor/benchmarks.md"]
        result = get_knowledge_summary(files)
        assert "2 files" in result
        assert "INDEX.md" in result
        assert "benchmarks.md" in result


class TestChatAPI:
    """Tests for POST /api/chat endpoint."""

    def test_chat_endpoint_exists(self):
        """POST /api/chat should return non-404."""
        resp = client.post("/api/chat", json={
            "equipment_type": "compressor",
            "question": "Test sorusu",
        })
        assert resp.status_code != 404

    def test_chat_empty_question_rejected(self):
        """Empty question should return 400."""
        resp = client.post("/api/chat", json={
            "equipment_type": "compressor",
            "question": "",
        })
        assert resp.status_code == 400

    def test_chat_whitespace_question_rejected(self):
        """Whitespace-only question should return 400."""
        resp = client.post("/api/chat", json={
            "equipment_type": "compressor",
            "question": "   ",
        })
        assert resp.status_code == 400

    def test_chat_request_schema(self):
        """Valid request should return non-404 and include expected keys."""
        resp = client.post("/api/chat", json={
            "equipment_type": "compressor",
            "subtype": "screw",
            "question": "Exergy verimi nasıl artırılır?",
            "analysis_data": {
                "metrics": {"exergy_efficiency_pct": 42.5},
            },
        })
        assert resp.status_code != 404
        data = resp.json()
        assert "answer" in data
        assert "knowledge_sources" in data
        assert "follow_up_suggestions" in data
        assert "ai_available" in data
