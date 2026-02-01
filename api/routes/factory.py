"""Factory project routes for ExergyLab API."""

import logging
import uuid
from datetime import datetime
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.schemas.factory import (
    AddEquipmentRequest,
    CreateFactoryProjectRequest,
    EquipmentItemResponse,
    FactoryAnalysisResponse,
    FactoryProjectResponse,
)
from engine.factory import EquipmentItem, analyze_factory

logger = logging.getLogger(__name__)

router = APIRouter()


# In-memory storage
_projects: dict[str, dict] = {}


# ---------------------------------------------------------------------------
# Interpret request model (local to this module)
# ---------------------------------------------------------------------------

class FactoryInterpretRequest(BaseModel):
    sector: str | None = None


# ---------------------------------------------------------------------------
# CRUD endpoints
# ---------------------------------------------------------------------------

@router.post("/factory/projects")
async def create_project(request: CreateFactoryProjectRequest):
    """Yeni fabrika projesi olustur."""
    project_id = str(uuid.uuid4())[:8]
    project = {
        "id": project_id,
        "name": request.name,
        "sector": request.sector,
        "description": request.description,
        "equipment": [],
        "created_at": datetime.utcnow().isoformat(),
    }
    _projects[project_id] = project
    return {"success": True, "project": _format_project(project)}


@router.get("/factory/projects")
async def list_projects():
    """Tum fabrika projelerini listele."""
    projects = [_format_project(p) for p in _projects.values()]
    return {"success": True, "projects": projects}


@router.get("/factory/projects/{project_id}")
async def get_project(project_id: str):
    """Fabrika projesini getir."""
    project = _projects.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"success": True, "project": _format_project(project)}


@router.post("/factory/projects/{project_id}/equipment")
async def add_equipment(project_id: str, request: AddEquipmentRequest):
    """Projeye ekipman ekle."""
    project = _projects.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    eq_id = str(uuid.uuid4())[:8]
    equipment = {
        "id": eq_id,
        "type": request.type.value,
        "subtype": request.subtype,
        "name": request.name,
        "parameters": request.parameters,
        "analysis_result": None,
    }
    project["equipment"].append(equipment)
    return {"success": True, "equipment": equipment}


@router.delete("/factory/projects/{project_id}/equipment/{equipment_id}")
async def remove_equipment(project_id: str, equipment_id: str):
    """Projeden ekipman kaldir."""
    project = _projects.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    original_len = len(project["equipment"])
    project["equipment"] = [
        eq for eq in project["equipment"] if eq["id"] != equipment_id
    ]
    if len(project["equipment"]) == original_len:
        raise HTTPException(status_code=404, detail="Equipment not found")

    return {"success": True}


# ---------------------------------------------------------------------------
# Analysis endpoint
# ---------------------------------------------------------------------------

@router.post("/factory/projects/{project_id}/analyze")
async def analyze_factory_project(project_id: str):
    """Fabrika seviyesi analiz calistir."""
    project = _projects.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if not project["equipment"]:
        raise HTTPException(status_code=400, detail="Project has no equipment")

    # Convert to engine EquipmentItem list
    items = []
    for eq in project["equipment"]:
        items.append(EquipmentItem(
            id=eq["id"],
            name=eq["name"],
            equipment_type=eq["type"],
            subtype=eq["subtype"],
            parameters=eq["parameters"],
        ))

    try:
        result = analyze_factory(items)
    except Exception as e:
        logger.exception("Factory analysis failed")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

    # Store individual analysis results back on equipment
    for eq_result in result.equipment_results:
        for eq in project["equipment"]:
            if eq["id"] == eq_result["id"]:
                eq["analysis_result"] = eq_result.get("analysis")

    response = {
        "success": True,
        "project_id": project_id,
        "equipment_results": result.equipment_results,
        "aggregates": result.aggregates,
        "hotspots": result.hotspots,
        "integration_opportunities": result.integration_opportunities,
        "sankey": result.sankey,
    }
    return response


# ---------------------------------------------------------------------------
# AI Interpretation endpoint
# ---------------------------------------------------------------------------

@router.post("/factory/projects/{project_id}/interpret")
async def interpret_factory(project_id: str, request: FactoryInterpretRequest = None):
    """Fabrika analizi AI yorumlama."""
    project = _projects.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Check if we have analysis results
    has_results = any(eq.get("analysis_result") for eq in project["equipment"])
    if not has_results:
        raise HTTPException(status_code=400, detail="Run analysis first")

    try:
        from api.services.claude_code_service import interpret_factory_analysis
        sector = (request.sector if request else None) or project.get("sector")

        interpretation = await interpret_factory_analysis(
            project=project,
            sector=sector,
        )
        return {"success": True, "interpretation": interpretation}
    except Exception:
        logger.exception("Factory interpretation failed")
        return {
            "success": False,
            "interpretation": {
                "ai_available": False,
                "summary": "",
                "hotspot_analysis": [],
                "integration_opportunities": [],
                "prioritized_actions": [],
                "sector_specific_insights": [],
                "warnings": [],
            },
        }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _format_project(project: dict) -> dict:
    """Format project for API response."""
    return {
        "id": project["id"],
        "name": project["name"],
        "sector": project.get("sector"),
        "description": project.get("description"),
        "equipment": project["equipment"],
        "created_at": project.get("created_at", ""),
        "equipment_count": len(project["equipment"]),
    }
