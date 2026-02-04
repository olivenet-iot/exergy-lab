"""CRUD operations for ExergyLab database."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api.database.models import (
    AIInterpretation,
    AnalysisResult,
    Equipment,
    FactoryAnalysis,
    FactoryProject,
    User,
)


# ---------------------------------------------------------------------------
# User CRUD
# ---------------------------------------------------------------------------

async def create_user(
    db: AsyncSession,
    email: str,
    hashed_password: str,
    full_name: str | None = None,
) -> User:
    """Create a new user."""
    user = User(email=email, hashed_password=hashed_password, full_name=full_name)
    db.add(user)
    await db.flush()
    return user


async def get_user(db: AsyncSession, user_id: str) -> User | None:
    """Get a user by ID."""
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    """Get a user by email."""
    stmt = select(User).where(User.email == email)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


# ---------------------------------------------------------------------------
# Project CRUD
# ---------------------------------------------------------------------------

async def create_project(
    db: AsyncSession,
    name: str,
    sector: str | None = None,
    description: str | None = None,
    owner_id: str | None = None,
) -> FactoryProject:
    """Create a new factory project."""
    project = FactoryProject(
        name=name, sector=sector, description=description, owner_id=owner_id
    )
    db.add(project)
    await db.flush()
    # Re-query with eager loading so relationships are accessible outside async
    return await get_project(db, project.id)  # type: ignore[return-value]


async def get_project(db: AsyncSession, project_id: str) -> FactoryProject | None:
    """Get a project by ID with equipment and analysis results eagerly loaded."""
    stmt = (
        select(FactoryProject)
        .where(FactoryProject.id == project_id)
        .options(
            selectinload(FactoryProject.equipment).selectinload(
                Equipment.analysis_result
            )
        )
    )
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_all_projects(
    db: AsyncSession, owner_id: str | None = None
) -> list[FactoryProject]:
    """Get all projects ordered by created_at desc.

    If owner_id is provided, return only projects owned by that user
    plus ownerless (legacy) projects.
    """
    stmt = (
        select(FactoryProject)
        .options(
            selectinload(FactoryProject.equipment).selectinload(
                Equipment.analysis_result
            )
        )
        .order_by(FactoryProject.created_at.desc())
    )
    if owner_id is not None:
        stmt = stmt.where(
            (FactoryProject.owner_id == owner_id)
            | (FactoryProject.owner_id.is_(None))
        )
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def delete_project(db: AsyncSession, project_id: str) -> bool:
    """Delete a project by ID. Returns True if deleted."""
    project = await get_project(db, project_id)
    if not project:
        return False
    await db.delete(project)
    await db.flush()
    return True


# ---------------------------------------------------------------------------
# Equipment CRUD
# ---------------------------------------------------------------------------

async def add_equipment(
    db: AsyncSession,
    project_id: str,
    name: str,
    equipment_type: str,
    subtype: str | None = None,
    parameters: dict | None = None,
) -> Equipment | None:
    """Add equipment to a project. Returns None if project not found."""
    project = await get_project(db, project_id)
    if not project:
        return None
    eq = Equipment(
        project_id=project_id,
        name=name,
        equipment_type=equipment_type,
        subtype=subtype,
        parameters=parameters or {},
    )
    db.add(eq)
    await db.flush()
    # Re-query with eager loading so analysis_result is accessible outside async
    stmt = (
        select(Equipment)
        .where(Equipment.id == eq.id)
        .options(selectinload(Equipment.analysis_result))
    )
    result = await db.execute(stmt)
    return result.scalar_one()


async def remove_equipment(
    db: AsyncSession, project_id: str, equipment_id: str
) -> bool:
    """Remove equipment from a project. Returns True if removed."""
    stmt = (
        select(Equipment)
        .where(Equipment.id == equipment_id, Equipment.project_id == project_id)
    )
    result = await db.execute(stmt)
    eq = result.scalar_one_or_none()
    if not eq:
        return False
    await db.delete(eq)
    await db.flush()
    return True


# ---------------------------------------------------------------------------
# Analysis CRUD
# ---------------------------------------------------------------------------

async def save_equipment_analysis(
    db: AsyncSession, equipment_id: str, result_data: dict
) -> AnalysisResult:
    """Save or update an equipment analysis result (upsert)."""
    stmt = select(AnalysisResult).where(
        AnalysisResult.equipment_id == equipment_id
    )
    result = await db.execute(stmt)
    existing = result.scalar_one_or_none()
    if existing:
        existing.result_data = result_data
        await db.flush()
        return existing
    ar = AnalysisResult(equipment_id=equipment_id, result_data=result_data)
    db.add(ar)
    await db.flush()
    return ar


async def save_factory_analysis(
    db: AsyncSession,
    project_id: str,
    aggregates: dict,
    hotspots: list,
    integration_opportunities: list,
    sankey: dict,
) -> FactoryAnalysis:
    """Save a factory-level analysis snapshot."""
    fa = FactoryAnalysis(
        project_id=project_id,
        aggregates=aggregates,
        hotspots=hotspots,
        integration_opportunities=integration_opportunities,
        sankey_data=sankey,
    )
    db.add(fa)
    await db.flush()
    return fa


async def save_ai_interpretation(
    db: AsyncSession,
    interpretation_data: dict,
    project_id: str | None = None,
    equipment_id: str | None = None,
) -> AIInterpretation:
    """Save an AI interpretation."""
    interp = AIInterpretation(
        project_id=project_id,
        equipment_id=equipment_id,
        interpretation_data=interpretation_data,
    )
    db.add(interp)
    await db.flush()
    return interp
