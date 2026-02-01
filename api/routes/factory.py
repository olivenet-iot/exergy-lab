"""Factory project routes for ExergyLab API."""

import uuid

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()


class EquipmentItem(BaseModel):
    id: str
    type: str
    subtype: str
    name: str
    parameters: dict
    analysis_result: Optional[dict] = None


class FactoryProject(BaseModel):
    id: Optional[str] = None
    name: str
    equipment: List[EquipmentItem] = []
    summary: Optional[dict] = None


# In-memory storage
_projects: dict[str, dict] = {}


@router.post("/factory/projects")
async def create_project(project: FactoryProject):
    """Yeni fabrika projesi olustur."""
    project.id = str(uuid.uuid4())[:8]
    _projects[project.id] = project.model_dump()
    return {"success": True, "project": _projects[project.id]}


@router.get("/factory/projects/{project_id}")
async def get_project(project_id: str):
    """Fabrika projesini getir."""
    if project_id not in _projects:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"success": True, "project": _projects[project_id]}
