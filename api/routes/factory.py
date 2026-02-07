"""Factory project routes for ExergyLab API."""

import logging

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.dependencies import get_current_user
from api.database import crud
from api.database.models import Equipment as EquipmentModel
from api.database.models import FactoryProject, User
from api.database.session import get_db
from api.schemas.factory import (
    AddEquipmentRequest,
    CreateFactoryProjectRequest,
    PinchAnalysisRequest,
    UpdateProcessRequest,
)
from engine.factory import EquipmentItem, analyze_factory

logger = logging.getLogger(__name__)

router = APIRouter()


# ---------------------------------------------------------------------------
# Interpret request model (local to this module)
# ---------------------------------------------------------------------------

class FactoryInterpretRequest(BaseModel):
    sector: str | None = None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _format_equipment(eq: EquipmentModel) -> dict:
    """Convert an Equipment ORM object to API-compatible dict."""
    return {
        "id": eq.id,
        "type": eq.equipment_type,
        "subtype": eq.subtype,
        "name": eq.name,
        "parameters": eq.parameters,
        "analysis_result": (
            eq.analysis_result.result_data if eq.analysis_result else None
        ),
    }


def _format_project(project: FactoryProject) -> dict:
    """Format project ORM object for API response."""
    return {
        "id": project.id,
        "name": project.name,
        "sector": project.sector,
        "description": project.description,
        "equipment": [_format_equipment(eq) for eq in project.equipment],
        "created_at": project.created_at.isoformat(),
        "equipment_count": len(project.equipment),
        "process_type": project.process_type,
        "process_label": project.process_label,
        "process_parameters": project.process_parameters,
        "process_subcategory": project.process_subcategory,
        "operating_hours": project.operating_hours,
        "energy_price_eur_kwh": project.energy_price_eur_kwh,
    }


def _check_ownership(project: FactoryProject, current_user: User | None) -> None:
    """Raise 403 if user is authenticated but doesn't own the project.

    Rules:
    - No user (unauthenticated) → allow (backward compat)
    - Project has no owner (legacy) → allow
    - User matches owner → allow
    - User doesn't match owner → 403
    """
    if current_user and project.owner_id and project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized for this project")


# ---------------------------------------------------------------------------
# CRUD endpoints
# ---------------------------------------------------------------------------

@router.post("/factory/projects")
async def create_project(
    request: CreateFactoryProjectRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Yeni fabrika projesi olustur."""
    project = await crud.create_project(
        db,
        name=request.name,
        sector=request.sector,
        description=request.description,
        owner_id=current_user.id if current_user else None,
    )
    # Set process fields if provided
    if request.process_type:
        await crud.update_project_process(
            db,
            project.id,
            process_type=request.process_type,
            process_label=request.process_label,
            process_parameters=request.process_parameters,
            process_subcategory=request.process_subcategory,
            operating_hours=request.operating_hours,
            energy_price_eur_kwh=request.energy_price_eur_kwh,
        )
        project = await crud.get_project(db, project.id)
    return {"success": True, "project": _format_project(project)}


@router.get("/factory/projects")
async def list_projects(
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Tum fabrika projelerini listele."""
    projects = await crud.get_all_projects(
        db, owner_id=current_user.id if current_user else None
    )
    return {"success": True, "projects": [_format_project(p) for p in projects]}


@router.get("/factory/projects/{project_id}")
async def get_project(
    project_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Fabrika projesini getir."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    _check_ownership(project, current_user)
    return {"success": True, "project": _format_project(project)}


@router.post("/factory/projects/{project_id}/equipment")
async def add_equipment(
    project_id: str,
    request: AddEquipmentRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Projeye ekipman ekle."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    _check_ownership(project, current_user)
    eq = await crud.add_equipment(
        db,
        project_id=project_id,
        name=request.name,
        equipment_type=request.type.value,
        subtype=request.subtype,
        parameters=request.parameters,
    )
    if eq is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"success": True, "equipment": _format_equipment(eq)}


@router.delete("/factory/projects/{project_id}/equipment/{equipment_id}")
async def remove_equipment(
    project_id: str,
    equipment_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Projeden ekipman kaldir."""
    # Check project exists first
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    _check_ownership(project, current_user)

    removed = await crud.remove_equipment(db, project_id, equipment_id)
    if not removed:
        raise HTTPException(status_code=404, detail="Equipment not found")

    return {"success": True}


# ---------------------------------------------------------------------------
# Analysis endpoint
# ---------------------------------------------------------------------------

@router.post("/factory/projects/{project_id}/analyze")
async def analyze_factory_project(
    project_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Fabrika seviyesi analiz calistir."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    _check_ownership(project, current_user)

    if not project.equipment:
        raise HTTPException(status_code=400, detail="Project has no equipment")

    # Convert ORM objects to engine EquipmentItem list
    items = []
    for eq in project.equipment:
        items.append(EquipmentItem(
            id=eq.id,
            name=eq.name,
            equipment_type=eq.equipment_type,
            subtype=eq.subtype,
            parameters=eq.parameters,
        ))

    try:
        result = analyze_factory(items)
    except Exception as e:
        logger.exception("Factory analysis failed")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

    # Store individual analysis results back on equipment
    for eq_result in result.equipment_results:
        for eq in project.equipment:
            if eq.id == eq_result["id"]:
                await crud.save_equipment_analysis(
                    db, eq.id, eq_result.get("analysis")
                )

    # Gap analysis (if process definition exists on project)
    gap_analysis_data = None
    if project.process_type:
        try:
            from engine.process_exergy import ProcessDefinition
            from engine.gap_analysis import analyze_gap

            process_def = ProcessDefinition(
                process_type=project.process_type,
                process_label=project.process_label or "",
                parameters=project.process_parameters or {},
                subcategory=project.process_subcategory or "general",
                operating_hours=project.operating_hours or 6000,
                energy_price_eur_kwh=project.energy_price_eur_kwh or 0.08,
            )

            gap_result = analyze_gap(
                process_def=process_def,
                equipment_results=result.equipment_results,
                aggregates=result.aggregates,
                hotspots=result.hotspots,
                energy_price_eur_kwh=process_def.energy_price_eur_kwh,
                operating_hours=process_def.operating_hours,
            )
            gap_analysis_data = gap_result.to_dict()
        except Exception:
            logger.exception("Gap analysis failed (non-critical)")

    response = {
        "success": True,
        "project_id": project_id,
        "equipment_results": result.equipment_results,
        "aggregates": result.aggregates,
        "hotspots": result.hotspots,
        "integration_opportunities": result.integration_opportunities,
        "sankey": result.sankey,
        "pinch_analysis": result.pinch_analysis,
        "advanced_exergy": result.advanced_exergy,
        "entropy_generation": result.entropy_generation,
        "thermoeconomic_optimization": result.thermoeconomic_optimization,
        "energy_management": result.energy_management,
        "gap_analysis": gap_analysis_data,
    }
    return response


# ---------------------------------------------------------------------------
# Process types / Gap analysis endpoints
# ---------------------------------------------------------------------------

@router.get("/factory/process-types")
async def get_process_types_endpoint():
    """Tüm desteklenen proses tiplerini döndürür."""
    from engine.process_exergy import get_process_types
    return {"success": True, "process_types": get_process_types()}


@router.get("/factory/process-types/{process_type}/subcategories")
async def get_subcategories_endpoint(process_type: str):
    """Bir proses tipi için BAT alt kategorilerini döndürür."""
    from engine.bat_references import get_available_subcategories
    try:
        subcategories = get_available_subcategories(process_type)
        return {"success": True, "subcategories": subcategories}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/factory/projects/{project_id}/process")
async def update_process_definition(
    project_id: str,
    request: UpdateProcessRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Mevcut projenin proses tanımını günceller."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    _check_ownership(project, current_user)

    project = await crud.update_project_process(
        db,
        project_id=project_id,
        process_type=request.process_type,
        process_label=request.process_label,
        process_parameters=request.process_parameters,
        process_subcategory=request.process_subcategory,
        operating_hours=request.operating_hours,
        energy_price_eur_kwh=request.energy_price_eur_kwh,
    )
    return {"success": True, "project": _format_project(project)}


# ---------------------------------------------------------------------------
# Pinch Analysis endpoint
# ---------------------------------------------------------------------------

@router.post("/factory/projects/{project_id}/pinch")
async def run_pinch_analysis(
    project_id: str,
    pinch_params: PinchAnalysisRequest = None,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Fabrika icin pinch analizi calistir (ozel parametreler ile)."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    _check_ownership(project, current_user)

    if not project.equipment:
        raise HTTPException(status_code=400, detail="Project has no equipment")

    # Check that we have analysis results
    has_results = any(eq.analysis_result for eq in project.equipment)
    if not has_results:
        raise HTTPException(status_code=400, detail="Run analysis first")

    # Build equipment list and results dict
    items = []
    results_dict = {}
    for eq in project.equipment:
        items.append(EquipmentItem(
            id=eq.id,
            name=eq.name,
            equipment_type=eq.equipment_type,
            subtype=eq.subtype,
            parameters=eq.parameters,
        ))
        if eq.analysis_result:
            results_dict[eq.id] = eq.analysis_result.result_data

    params = pinch_params or PinchAnalysisRequest()

    try:
        from engine.pinch import analyze_pinch

        pinch_result = analyze_pinch(
            items,
            results_dict,
            delta_T_min_C=params.delta_T_min_C,
            fuel_price_eur_kwh=params.fuel_price_eur_kwh,
            operating_hours=params.operating_hours,
            include_pumps=params.include_pumps,
        )
        return {"success": True, "pinch_analysis": pinch_result.to_dict()}
    except Exception as e:
        logger.exception("Pinch analysis failed")
        raise HTTPException(status_code=500, detail=f"Pinch analysis failed: {str(e)}")


# ---------------------------------------------------------------------------
# Advanced Exergy endpoint
# ---------------------------------------------------------------------------

@router.post("/factory/projects/{project_id}/advanced-exergy")
async def run_advanced_exergy(
    project_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Fabrika icin ileri exergy analizi (EN/EX dekompozisyon) calistir."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    _check_ownership(project, current_user)

    if not project.equipment:
        raise HTTPException(status_code=400, detail="Project has no equipment")

    has_results = any(eq.analysis_result for eq in project.equipment)
    if not has_results:
        raise HTTPException(status_code=400, detail="Run analysis first")

    eq_list_dicts = []
    results_dict = {}
    for eq in project.equipment:
        eq_list_dicts.append({
            "id": eq.id,
            "name": eq.name,
            "equipment_type": eq.equipment_type,
            "subtype": eq.subtype,
            "parameters": eq.parameters,
        })
        if eq.analysis_result:
            results_dict[eq.id] = eq.analysis_result.result_data

    try:
        from engine.advanced_exergy import analyze_advanced_exergy

        adv_result = analyze_advanced_exergy(eq_list_dicts, results_dict)
        return {"success": True, "advanced_exergy": adv_result.to_dict()}
    except Exception as e:
        logger.exception("Advanced exergy analysis failed")
        raise HTTPException(status_code=500, detail=f"Advanced exergy analysis failed: {str(e)}")


# ---------------------------------------------------------------------------
# Entropy Generation (EGM) endpoint
# ---------------------------------------------------------------------------

@router.post("/factory/projects/{project_id}/entropy-generation")
async def run_entropy_generation(
    project_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Fabrika icin entropi uretimi minimizasyonu (EGM) analizi calistir."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    _check_ownership(project, current_user)

    if not project.equipment:
        raise HTTPException(status_code=400, detail="Project has no equipment")

    has_results = any(eq.analysis_result for eq in project.equipment)
    if not has_results:
        raise HTTPException(status_code=400, detail="Run analysis first")

    eq_list_dicts = []
    results_dict = {}
    for eq in project.equipment:
        eq_list_dicts.append({
            "id": eq.id,
            "name": eq.name,
            "equipment_type": eq.equipment_type,
            "subtype": eq.subtype,
            "parameters": eq.parameters,
        })
        if eq.analysis_result:
            results_dict[eq.id] = eq.analysis_result.result_data

    try:
        from engine.entropy_generation import analyze_entropy_generation

        egm_result = analyze_entropy_generation(eq_list_dicts, results_dict)
        return {"success": True, "entropy_generation": egm_result.to_dict()}
    except Exception as e:
        logger.exception("Entropy generation analysis failed")
        raise HTTPException(status_code=500, detail=f"EGM analysis failed: {str(e)}")


# ---------------------------------------------------------------------------
# Thermoeconomic Optimization endpoint
# ---------------------------------------------------------------------------

@router.post("/factory/projects/{project_id}/thermoeconomic-optimization")
async def run_thermoeconomic_optimization(
    project_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Fabrika icin termoekonomik optimizasyon analizi calistir."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    _check_ownership(project, current_user)

    if not project.equipment:
        raise HTTPException(status_code=400, detail="Project has no equipment")

    has_results = any(eq.analysis_result for eq in project.equipment)
    if not has_results:
        raise HTTPException(status_code=400, detail="Run analysis first")

    eq_list_dicts = []
    results_dict = {}
    for eq in project.equipment:
        eq_list_dicts.append({
            "id": eq.id,
            "name": eq.name,
            "equipment_type": eq.equipment_type,
            "subtype": eq.subtype,
            "parameters": eq.parameters,
        })
        if eq.analysis_result:
            results_dict[eq.id] = eq.analysis_result.result_data

    try:
        from engine.thermoeconomic_optimization import analyze_thermoeconomic_optimization

        thermo_result = analyze_thermoeconomic_optimization(eq_list_dicts, results_dict)
        return {"success": True, "thermoeconomic_optimization": thermo_result.to_dict()}
    except Exception as e:
        logger.exception("Thermoeconomic optimization failed")
        raise HTTPException(status_code=500, detail=f"Thermoeconomic optimization failed: {str(e)}")


# ---------------------------------------------------------------------------
# Energy Management (ISO 50001) endpoint
# ---------------------------------------------------------------------------

@router.post("/factory/projects/{project_id}/energy-management")
async def run_energy_management(
    project_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Fabrika icin ISO 50001 enerji yonetimi degerlendirmesi calistir."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    _check_ownership(project, current_user)

    if not project.equipment:
        raise HTTPException(status_code=400, detail="Project has no equipment")

    has_results = any(eq.analysis_result for eq in project.equipment)
    if not has_results:
        raise HTTPException(status_code=400, detail="Run analysis first")

    # Build equipment list and results for previous motors
    items = []
    eq_list_dicts = []
    results_dict = {}
    for eq in project.equipment:
        items.append(EquipmentItem(
            id=eq.id,
            name=eq.name,
            equipment_type=eq.equipment_type,
            subtype=eq.subtype,
            parameters=eq.parameters,
        ))
        eq_list_dicts.append({
            "id": eq.id,
            "name": eq.name,
            "equipment_type": eq.equipment_type,
            "subtype": eq.subtype,
            "parameters": eq.parameters,
        })
        if eq.analysis_result:
            results_dict[eq.id] = eq.analysis_result.result_data

    try:
        from engine.energy_management import analyze_energy_management

        # Build equipment_results list matching factory pipeline format
        equipment_results = []
        for eq in project.equipment:
            entry = {
                "id": eq.id,
                "name": eq.name,
                "equipment_type": eq.equipment_type,
                "subtype": eq.subtype,
                "analysis": eq.analysis_result.result_data if eq.analysis_result else None,
            }
            equipment_results.append(entry)

        from engine.factory import _calculate_aggregates
        valid_results = [r for r in equipment_results if r.get("analysis")]
        aggregates = _calculate_aggregates(valid_results)

        # Run previous motors to get their results
        pinch_analysis = None
        try:
            from engine.pinch import analyze_pinch, extract_thermal_streams, check_pinch_feasibility
            streams = extract_thermal_streams(items, results_dict)
            feasible, _ = check_pinch_feasibility(streams)
            if feasible:
                pinch_result = analyze_pinch(items, results_dict)
                if pinch_result.is_valid:
                    pinch_analysis = pinch_result.to_dict()
        except Exception:
            pass

        advanced_exergy = None
        try:
            from engine.advanced_exergy import analyze_advanced_exergy, check_advanced_exergy_feasibility
            feasible, _ = check_advanced_exergy_feasibility(eq_list_dicts, results_dict)
            if feasible:
                adv_result = analyze_advanced_exergy(eq_list_dicts, results_dict)
                if adv_result.is_valid:
                    advanced_exergy = adv_result.to_dict()
        except Exception:
            pass

        entropy_generation = None
        try:
            from engine.entropy_generation import analyze_entropy_generation, check_egm_feasibility
            feasible, _ = check_egm_feasibility(eq_list_dicts, results_dict)
            if feasible:
                egm_result = analyze_entropy_generation(eq_list_dicts, results_dict)
                if egm_result.is_valid:
                    entropy_generation = egm_result.to_dict()
        except Exception:
            pass

        thermoeconomic_optimization = None
        try:
            from engine.thermoeconomic_optimization import analyze_thermoeconomic_optimization, check_thermoeconomic_feasibility
            feasible, _ = check_thermoeconomic_feasibility(eq_list_dicts, results_dict)
            if feasible:
                thermo_result = analyze_thermoeconomic_optimization(eq_list_dicts, results_dict)
                if thermo_result.is_valid:
                    thermoeconomic_optimization = thermo_result.to_dict()
        except Exception:
            pass

        factory_dict = {
            "equipment_results": equipment_results,
            "aggregates": aggregates,
            "pinch_analysis": pinch_analysis,
            "advanced_exergy": advanced_exergy,
            "entropy_generation": entropy_generation,
            "thermoeconomic_optimization": thermoeconomic_optimization,
        }

        em_result = analyze_energy_management(factory_dict)
        return {"success": True, "energy_management": em_result.to_dict()}
    except Exception as e:
        logger.exception("Energy management analysis failed")
        raise HTTPException(status_code=500, detail=f"Energy management analysis failed: {str(e)}")


# ---------------------------------------------------------------------------
# AI Interpretation endpoint
# ---------------------------------------------------------------------------

@router.post("/factory/projects/{project_id}/interpret")
async def interpret_factory(
    project_id: str,
    request: FactoryInterpretRequest = None,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user),
):
    """Fabrika analizi AI yorumlama."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    _check_ownership(project, current_user)

    # Check if we have analysis results
    has_results = any(eq.analysis_result for eq in project.equipment)
    if not has_results:
        raise HTTPException(status_code=400, detail="Run analysis first")

    try:
        from api.services.claude_code_service import interpret_factory_analysis

        sector = (request.sector if request else None) or project.sector

        # Reconstruct dict matching what _format_factory_analysis expects
        project_dict = {
            "id": project.id,
            "name": project.name,
            "sector": project.sector,
            "equipment": [_format_equipment(eq) for eq in project.equipment],
        }

        interpretation = await interpret_factory_analysis(
            project=project_dict,
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
