# Brief 20: Database Layer — SQLite ile Kalıcı Depolama

> **Claude Code için:** Bu brief'i oku ve uygula. In-memory storage'dan SQLite veritabanına geç. Factory projeleri, ekipmanlar, analiz sonuçları ve AI yorumları artık kalıcı olacak. Server restart'ta veri kaybolmayacak.

---

## 🎯 Hedef

**Mevcut durum:** `api/routes/factory.py` içinde `PROJECTS = {}` dict'i ile in-memory storage. Server restart = veri kaybı.

**Hedef:** SQLite + SQLAlchemy ile kalıcı depolama. Aynı API contract korunacak — frontend değişikliği yok.

**Scope:** Sadece database layer. Auth sonraki brief'te (Brief 21).

---

## ⚠️ OTONOM YETKİ

1. Brief'teki görevleri tamamla
2. Mevcut API endpoint'lerinin **request/response yapısını BOZMA** — frontend çalışmaya devam etmeli
3. 431 testi BOZMA (adaptasyon gerekebilir)
4. SQLAlchemy ve alembic dışında yeni paket EKLEME
5. Backend testleri database ile çalışacak şekilde güncelle

---

## 📋 Adım 0: Mevcut Durumu Anla (KRİTİK)

```bash
# 1. Factory routes — in-memory PROJECTS dict
cat api/routes/factory.py

# 2. Factory schemas — Pydantic models
cat api/schemas/factory.py

# 3. Main app — nasıl mount ediliyor
cat api/main.py

# 4. Mevcut test fixtures
cat tests/conftest.py

# 5. Factory API testleri — hangi endpoint'ler test ediliyor
cat tests/test_api.py | grep -A 50 "class TestFactoryAPI"

# 6. Requirements — mevcut dependencies
cat requirements.txt

# 7. Project structure
ls -la api/
```

---

## 🗄️ Veritabanı Şeması

### Tablolar

```
┌─────────────────────────────────────────────────────────────────┐
│ factory_projects                                                │
├─────────────────────────────────────────────────────────────────┤
│ id: UUID (PK)                                                   │
│ name: VARCHAR(255) NOT NULL                                     │
│ sector: VARCHAR(50)                                             │
│ description: TEXT                                               │
│ created_at: DATETIME                                            │
│ updated_at: DATETIME                                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ 1:N
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ equipment                                                        │
├─────────────────────────────────────────────────────────────────┤
│ id: UUID (PK)                                                   │
│ project_id: UUID (FK → factory_projects.id)                     │
│ name: VARCHAR(255) NOT NULL                                     │
│ equipment_type: VARCHAR(50) NOT NULL                            │
│ subtype: VARCHAR(50)                                            │
│ parameters: JSON NOT NULL                                       │
│ created_at: DATETIME                                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ 1:1
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ analysis_results                                                 │
├─────────────────────────────────────────────────────────────────┤
│ id: UUID (PK)                                                   │
│ equipment_id: UUID (FK → equipment.id, UNIQUE)                  │
│ result_data: JSON NOT NULL  -- full analysis result             │
│ analyzed_at: DATETIME                                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ factory_analyses                                                 │
├─────────────────────────────────────────────────────────────────┤
│ id: UUID (PK)                                                   │
│ project_id: UUID (FK → factory_projects.id)                     │
│ aggregates: JSON             -- total metrics                   │
│ hotspots: JSON               -- priority list                   │
│ integration_opportunities: JSON                                  │
│ sankey_data: JSON                                               │
│ analyzed_at: DATETIME                                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ ai_interpretations                                               │
├─────────────────────────────────────────────────────────────────┤
│ id: UUID (PK)                                                   │
│ project_id: UUID (FK, nullable) -- factory interpretation       │
│ equipment_id: UUID (FK, nullable) -- equipment interpretation   │
│ interpretation_data: JSON NOT NULL                              │
│ created_at: DATETIME                                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 Dosya Yapısı

```
api/
├── database/                    # YENİ dizin
│   ├── __init__.py             # Database exports
│   ├── config.py               # Database configuration
│   ├── models.py               # SQLAlchemy models
│   ├── session.py              # Session management
│   └── crud.py                 # CRUD operations
├── routes/
│   └── factory.py              # GÜNCELLEME — CRUD fonksiyonları kullan
├── main.py                     # GÜNCELLEME — database init
└── ...
```

---

## 📦 Adım 1: Dependencies

### `requirements.txt` — Eklemeler

```
# Mevcut dependencies...

# Database
sqlalchemy>=2.0.0
aiosqlite>=0.19.0
```

**NOT:** `alembic` migration tool'u şimdilik ekleme — basit tutuyoruz. Schema değişikliğinde manuel handle edilecek veya `create_all()` kullanılacak.

---

## 📦 Adım 2: Database Configuration

### `api/database/config.py`

```python
"""
Database configuration.
SQLite for development, can be switched to PostgreSQL for production.
"""
import os

# Database URL — SQLite file in project root
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite+aiosqlite:///./exergylab.db"
)

# For sync operations (if needed)
SYNC_DATABASE_URL = DATABASE_URL.replace("+aiosqlite", "")
```

---

## 📦 Adım 3: SQLAlchemy Models

### `api/database/models.py`

```python
"""
SQLAlchemy ORM models for ExergyLab.
"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.sqlite import JSON as SQLiteJSON

Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


class FactoryProject(Base):
    __tablename__ = "factory_projects"
    
    id = Column(String(36), primary_key=True, default=generate_uuid)
    name = Column(String(255), nullable=False)
    sector = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    equipment = relationship("Equipment", back_populates="project", cascade="all, delete-orphan")
    factory_analyses = relationship("FactoryAnalysis", back_populates="project", cascade="all, delete-orphan")
    ai_interpretations = relationship("AIInterpretation", back_populates="project", cascade="all, delete-orphan")


class Equipment(Base):
    __tablename__ = "equipment"
    
    id = Column(String(36), primary_key=True, default=generate_uuid)
    project_id = Column(String(36), ForeignKey("factory_projects.id"), nullable=False)
    name = Column(String(255), nullable=False)
    equipment_type = Column(String(50), nullable=False)
    subtype = Column(String(50), nullable=True)
    parameters = Column(JSON, nullable=False, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    project = relationship("FactoryProject", back_populates="equipment")
    analysis_result = relationship("AnalysisResult", back_populates="equipment", uselist=False, cascade="all, delete-orphan")
    ai_interpretations = relationship("AIInterpretation", back_populates="equipment", cascade="all, delete-orphan")


class AnalysisResult(Base):
    __tablename__ = "analysis_results"
    
    id = Column(String(36), primary_key=True, default=generate_uuid)
    equipment_id = Column(String(36), ForeignKey("equipment.id"), unique=True, nullable=False)
    result_data = Column(JSON, nullable=False)  # Full analysis result
    analyzed_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    equipment = relationship("Equipment", back_populates="analysis_result")


class FactoryAnalysis(Base):
    __tablename__ = "factory_analyses"
    
    id = Column(String(36), primary_key=True, default=generate_uuid)
    project_id = Column(String(36), ForeignKey("factory_projects.id"), nullable=False)
    aggregates = Column(JSON, nullable=True)
    hotspots = Column(JSON, nullable=True)
    integration_opportunities = Column(JSON, nullable=True)
    sankey_data = Column(JSON, nullable=True)
    analyzed_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    project = relationship("FactoryProject", back_populates="factory_analyses")


class AIInterpretation(Base):
    __tablename__ = "ai_interpretations"
    
    id = Column(String(36), primary_key=True, default=generate_uuid)
    project_id = Column(String(36), ForeignKey("factory_projects.id"), nullable=True)
    equipment_id = Column(String(36), ForeignKey("equipment.id"), nullable=True)
    interpretation_data = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    project = relationship("FactoryProject", back_populates="ai_interpretations")
    equipment = relationship("Equipment", back_populates="ai_interpretations")
```

---

## 📦 Adım 4: Session Management

### `api/database/session.py`

```python
"""
Database session management.
Async SQLAlchemy session for FastAPI.
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

from api.database.config import DATABASE_URL
from api.database.models import Base

# Async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # Set True for SQL logging during debug
    future=True,
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def init_db():
    """Create all tables."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_db():
    """Close database connections."""
    await engine.dispose()


@asynccontextmanager
async def get_session():
    """Get async database session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


# Dependency for FastAPI
async def get_db():
    """FastAPI dependency for database session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
```

---

## 📦 Adım 5: CRUD Operations

### `api/database/crud.py`

```python
"""
CRUD operations for database models.
"""
from typing import Optional, List
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api.database.models import (
    FactoryProject, Equipment, AnalysisResult,
    FactoryAnalysis, AIInterpretation
)


# ─── Factory Projects ───────────────────────────────────────────

async def create_project(
    db: AsyncSession,
    name: str,
    sector: Optional[str] = None,
    description: Optional[str] = None
) -> FactoryProject:
    """Create a new factory project."""
    project = FactoryProject(name=name, sector=sector, description=description)
    db.add(project)
    await db.flush()
    await db.refresh(project)
    return project


async def get_project(db: AsyncSession, project_id: str) -> Optional[FactoryProject]:
    """Get project by ID with equipment loaded."""
    result = await db.execute(
        select(FactoryProject)
        .options(selectinload(FactoryProject.equipment))
        .where(FactoryProject.id == project_id)
    )
    return result.scalar_one_or_none()


async def get_all_projects(db: AsyncSession) -> List[FactoryProject]:
    """Get all projects."""
    result = await db.execute(
        select(FactoryProject)
        .options(selectinload(FactoryProject.equipment))
        .order_by(FactoryProject.created_at.desc())
    )
    return list(result.scalars().all())


async def delete_project(db: AsyncSession, project_id: str) -> bool:
    """Delete project and all related data."""
    project = await get_project(db, project_id)
    if not project:
        return False
    await db.delete(project)
    return True


# ─── Equipment ──────────────────────────────────────────────────

async def add_equipment(
    db: AsyncSession,
    project_id: str,
    name: str,
    equipment_type: str,
    subtype: Optional[str] = None,
    parameters: dict = None
) -> Optional[Equipment]:
    """Add equipment to a project."""
    project = await get_project(db, project_id)
    if not project:
        return None
    
    equipment = Equipment(
        project_id=project_id,
        name=name,
        equipment_type=equipment_type,
        subtype=subtype,
        parameters=parameters or {}
    )
    db.add(equipment)
    await db.flush()
    await db.refresh(equipment)
    return equipment


async def get_equipment(db: AsyncSession, equipment_id: str) -> Optional[Equipment]:
    """Get equipment by ID."""
    result = await db.execute(
        select(Equipment).where(Equipment.id == equipment_id)
    )
    return result.scalar_one_or_none()


async def remove_equipment(db: AsyncSession, project_id: str, equipment_id: str) -> bool:
    """Remove equipment from project."""
    result = await db.execute(
        select(Equipment)
        .where(Equipment.id == equipment_id)
        .where(Equipment.project_id == project_id)
    )
    equipment = result.scalar_one_or_none()
    if not equipment:
        return False
    await db.delete(equipment)
    return True


# ─── Analysis Results ───────────────────────────────────────────

async def save_equipment_analysis(
    db: AsyncSession,
    equipment_id: str,
    result_data: dict
) -> AnalysisResult:
    """Save or update equipment analysis result."""
    # Check if exists
    result = await db.execute(
        select(AnalysisResult).where(AnalysisResult.equipment_id == equipment_id)
    )
    existing = result.scalar_one_or_none()
    
    if existing:
        existing.result_data = result_data
        existing.analyzed_at = datetime.utcnow()
        await db.flush()
        return existing
    else:
        analysis = AnalysisResult(
            equipment_id=equipment_id,
            result_data=result_data
        )
        db.add(analysis)
        await db.flush()
        await db.refresh(analysis)
        return analysis


async def get_equipment_analysis(
    db: AsyncSession,
    equipment_id: str
) -> Optional[dict]:
    """Get equipment analysis result."""
    result = await db.execute(
        select(AnalysisResult).where(AnalysisResult.equipment_id == equipment_id)
    )
    analysis = result.scalar_one_or_none()
    return analysis.result_data if analysis else None


# ─── Factory Analysis ───────────────────────────────────────────

async def save_factory_analysis(
    db: AsyncSession,
    project_id: str,
    aggregates: dict,
    hotspots: list,
    integration_opportunities: list,
    sankey_data: dict
) -> FactoryAnalysis:
    """Save factory-level analysis."""
    # Delete old analysis
    await db.execute(
        delete(FactoryAnalysis).where(FactoryAnalysis.project_id == project_id)
    )
    
    analysis = FactoryAnalysis(
        project_id=project_id,
        aggregates=aggregates,
        hotspots=hotspots,
        integration_opportunities=integration_opportunities,
        sankey_data=sankey_data
    )
    db.add(analysis)
    await db.flush()
    await db.refresh(analysis)
    return analysis


async def get_factory_analysis(
    db: AsyncSession,
    project_id: str
) -> Optional[FactoryAnalysis]:
    """Get latest factory analysis."""
    result = await db.execute(
        select(FactoryAnalysis)
        .where(FactoryAnalysis.project_id == project_id)
        .order_by(FactoryAnalysis.analyzed_at.desc())
    )
    return result.scalar_one_or_none()


# ─── AI Interpretations ─────────────────────────────────────────

async def save_ai_interpretation(
    db: AsyncSession,
    interpretation_data: dict,
    project_id: Optional[str] = None,
    equipment_id: Optional[str] = None
) -> AIInterpretation:
    """Save AI interpretation."""
    interpretation = AIInterpretation(
        project_id=project_id,
        equipment_id=equipment_id,
        interpretation_data=interpretation_data
    )
    db.add(interpretation)
    await db.flush()
    await db.refresh(interpretation)
    return interpretation


async def get_ai_interpretation(
    db: AsyncSession,
    project_id: Optional[str] = None,
    equipment_id: Optional[str] = None
) -> Optional[dict]:
    """Get latest AI interpretation."""
    query = select(AIInterpretation)
    if project_id:
        query = query.where(AIInterpretation.project_id == project_id)
    if equipment_id:
        query = query.where(AIInterpretation.equipment_id == equipment_id)
    query = query.order_by(AIInterpretation.created_at.desc())
    
    result = await db.execute(query)
    interpretation = result.scalar_one_or_none()
    return interpretation.interpretation_data if interpretation else None


# Import datetime for analysis updates
from datetime import datetime
```

---

## 📦 Adım 6: Database Init

### `api/database/__init__.py`

```python
"""
Database module exports.
"""
from api.database.config import DATABASE_URL
from api.database.models import Base, FactoryProject, Equipment, AnalysisResult, FactoryAnalysis, AIInterpretation
from api.database.session import init_db, close_db, get_db, get_session
from api.database import crud

__all__ = [
    "DATABASE_URL",
    "Base",
    "FactoryProject",
    "Equipment", 
    "AnalysisResult",
    "FactoryAnalysis",
    "AIInterpretation",
    "init_db",
    "close_db",
    "get_db",
    "get_session",
    "crud",
]
```

---

## 📦 Adım 7: Main App Update

### `api/main.py` — Güncelleme

```python
# Mevcut import'lara EKLE:
from contextlib import asynccontextmanager
from api.database.session import init_db, close_db

# Lifespan context manager (yeni FastAPI pattern)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown
    await close_db()

# App oluştururken lifespan ekle:
app = FastAPI(
    title="ExergyLab API",
    ...,
    lifespan=lifespan  # EKLENDİ
)
```

---

## 📦 Adım 8: Factory Routes Update

### `api/routes/factory.py` — MAJOR UPDATE

Mevcut in-memory `PROJECTS = {}` yerine database CRUD kullan.

**Strateji:** Her endpoint'i tek tek güncelle. API response yapısı AYNI kalacak.

```python
"""
Factory routes — updated to use database.
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.database.session import get_db
from api.database import crud
from api.schemas.factory import (
    FactoryProjectCreate, FactoryProjectResponse,
    EquipmentCreate, EquipmentResponse
)
# ... diğer import'lar

router = APIRouter(prefix="/factory", tags=["factory"])


# ─── Project CRUD ───────────────────────────────────────────────

@router.post("", response_model=FactoryProjectResponse)
async def create_project(
    project: FactoryProjectCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new factory project."""
    db_project = await crud.create_project(
        db,
        name=project.name,
        sector=project.sector,
        description=project.description
    )
    return _project_to_response(db_project)


@router.get("", response_model=list[FactoryProjectResponse])
async def list_projects(db: AsyncSession = Depends(get_db)):
    """List all factory projects."""
    projects = await crud.get_all_projects(db)
    return [_project_to_response(p) for p in projects]


@router.get("/{project_id}", response_model=FactoryProjectResponse)
async def get_project(project_id: str, db: AsyncSession = Depends(get_db)):
    """Get a factory project by ID."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(404, "Project not found")
    return _project_to_response(project)


@router.delete("/{project_id}")
async def delete_project(project_id: str, db: AsyncSession = Depends(get_db)):
    """Delete a factory project."""
    deleted = await crud.delete_project(db, project_id)
    if not deleted:
        raise HTTPException(404, "Project not found")
    return {"status": "deleted"}


# ─── Equipment CRUD ─────────────────────────────────────────────

@router.post("/{project_id}/equipment", response_model=EquipmentResponse)
async def add_equipment(
    project_id: str,
    equipment: EquipmentCreate,
    db: AsyncSession = Depends(get_db)
):
    """Add equipment to a project."""
    db_equipment = await crud.add_equipment(
        db,
        project_id=project_id,
        name=equipment.name,
        equipment_type=equipment.equipment_type,
        subtype=equipment.subtype,
        parameters=equipment.parameters
    )
    if not db_equipment:
        raise HTTPException(404, "Project not found")
    return _equipment_to_response(db_equipment)


@router.delete("/{project_id}/equipment/{equipment_id}")
async def remove_equipment(
    project_id: str,
    equipment_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Remove equipment from a project."""
    removed = await crud.remove_equipment(db, project_id, equipment_id)
    if not removed:
        raise HTTPException(404, "Equipment not found")
    return {"status": "removed"}


# ─── Analysis ───────────────────────────────────────────────────

@router.post("/{project_id}/analyze")
async def analyze_factory(project_id: str, db: AsyncSession = Depends(get_db)):
    """Run analysis on all equipment in a factory."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(404, "Project not found")
    
    if not project.equipment:
        raise HTTPException(400, "No equipment to analyze")
    
    # Convert equipment to analysis format
    equipment_list = [
        {
            "id": eq.id,
            "name": eq.name,
            "type": eq.equipment_type,
            "subtype": eq.subtype,
            "parameters": eq.parameters
        }
        for eq in project.equipment
    ]
    
    # Run factory analysis (existing engine)
    from engine.factory import analyze_factory as run_factory_analysis
    result = run_factory_analysis(equipment_list)
    
    # Save results
    await crud.save_factory_analysis(
        db,
        project_id=project_id,
        aggregates=result.get("aggregates", {}),
        hotspots=result.get("hotspots", []),
        integration_opportunities=result.get("integration_opportunities", []),
        sankey_data=result.get("sankey", {})
    )
    
    # Save individual equipment results
    for eq_result in result.get("equipment_results", []):
        eq_id = eq_result.get("equipment_id")
        if eq_id:
            await crud.save_equipment_analysis(db, eq_id, eq_result)
    
    return result


@router.post("/{project_id}/interpret")
async def interpret_factory(project_id: str, db: AsyncSession = Depends(get_db)):
    """Get AI interpretation for factory analysis."""
    # Check if analysis exists
    factory_analysis = await crud.get_factory_analysis(db, project_id)
    if not factory_analysis:
        raise HTTPException(400, "Run analysis first")
    
    # Check for cached interpretation
    cached = await crud.get_ai_interpretation(db, project_id=project_id)
    if cached:
        return cached
    
    # Get project for context
    project = await crud.get_project(db, project_id)
    
    # Build analysis data for AI
    analysis_data = {
        "factory_name": project.name,
        "sector": project.sector,
        "aggregates": factory_analysis.aggregates,
        "hotspots": factory_analysis.hotspots,
        "integration_opportunities": factory_analysis.integration_opportunities,
        "equipment_count": len(project.equipment)
    }
    
    # Call AI service
    from api.services.claude_code_service import interpret_factory_analysis
    interpretation = await interpret_factory_analysis(analysis_data)
    
    # Cache interpretation
    await crud.save_ai_interpretation(
        db,
        interpretation_data=interpretation,
        project_id=project_id
    )
    
    return interpretation


# ─── Helper Functions ───────────────────────────────────────────

def _project_to_response(project: "FactoryProject") -> dict:
    """Convert DB model to API response."""
    return {
        "id": project.id,
        "name": project.name,
        "sector": project.sector,
        "description": project.description,
        "equipment": [_equipment_to_response(eq) for eq in project.equipment],
        "created_at": project.created_at.isoformat() if project.created_at else None,
        "updated_at": project.updated_at.isoformat() if project.updated_at else None,
    }


def _equipment_to_response(equipment: "Equipment") -> dict:
    """Convert DB model to API response."""
    return {
        "id": equipment.id,
        "name": equipment.name,
        "equipment_type": equipment.equipment_type,
        "subtype": equipment.subtype,
        "parameters": equipment.parameters,
    }
```

---

## 📦 Adım 9: Test Fixtures Update

### `tests/conftest.py` — Database Test Setup

```python
"""
Test fixtures with database support.
"""
import pytest
import asyncio
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from api.main import app
from api.database.models import Base
from api.database.session import get_db

# Test database (in-memory SQLite)
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestSessionLocal = sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture(scope="function")
def client():
    """Test client with fresh database for each test."""
    
    async def override_get_db():
        async with TestSessionLocal() as session:
            yield session
    
    # Create tables
    async def setup_db():
        async with test_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    
    async def teardown_db():
        async with test_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
    
    # Run setup
    asyncio.get_event_loop().run_until_complete(setup_db())
    
    # Override dependency
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    # Cleanup
    app.dependency_overrides.clear()
    asyncio.get_event_loop().run_until_complete(teardown_db())
```

**NOT:** Mevcut testler `client` fixture'ı kullanıyorsa çalışmaya devam edecek. Database her test için sıfırlanıyor (isolation).

---

## 📦 Adım 10: Requirements Update

```bash
# requirements.txt'e ekle:
echo "sqlalchemy>=2.0.0" >> requirements.txt
echo "aiosqlite>=0.19.0" >> requirements.txt

# Install
pip install sqlalchemy aiosqlite
```

---

## 📋 Uygulama Sırası

### Faz 1: Keşif
1. Mevcut factory.py route'unu oku — PROJECTS dict yapısı
2. Mevcut schema'ları oku
3. Mevcut testleri oku — hangi endpoint'ler test ediliyor

### Faz 2: Database Altyapısı
4. `api/database/` dizini oluştur
5. `api/database/config.py` — DATABASE_URL
6. `api/database/models.py` — SQLAlchemy models
7. `api/database/session.py` — Async session, init_db, get_db
8. `api/database/crud.py` — CRUD operations
9. `api/database/__init__.py` — Exports

### Faz 3: Integration
10. `api/main.py` — Lifespan ile database init
11. `requirements.txt` — sqlalchemy, aiosqlite
12. `pip install sqlalchemy aiosqlite`

### Faz 4: Routes Migration
13. `api/routes/factory.py` — MAJOR UPDATE
    - `PROJECTS = {}` kaldır
    - Her endpoint'i CRUD ile değiştir
    - Response yapısını KORU

### Faz 5: Tests
14. `tests/conftest.py` — Test database fixture
15. `pytest tests/ -v` — Mevcut testler geçmeli

### Faz 6: Verification
16. Manual test: 
    - Factory oluştur
    - Ekipman ekle
    - Server restart
    - Factory hâlâ orada!
17. `npx vite build` — Frontend build (değişiklik yok)
18. `git add -A && git commit && git push`

---

## ⚠️ Dikkat Edilecekler

1. **API Contract korunmalı.** Frontend hiçbir değişiklik yapmadan çalışmalı. Response JSON yapısı aynı kalmalı.

2. **Async/await tutarlılığı.** SQLAlchemy 2.0 async kullanıyoruz. Tüm database işlemleri `await` ile.

3. **Test isolation.** Her test kendi database'i ile çalışmalı. `scope="function"` ile her test için yeni database.

4. **Error handling.** Database hataları uygun HTTP status code'larıyla dönmeli (404, 500).

5. **JSON serialization.** SQLAlchemy model'leri doğrudan JSON'a serialize edilmez — helper fonksiyonlar kullan.

6. **Migration yok.** Schema değişikliklerinde `create_all()` yeterli (development). Production'da alembic eklenebilir.

---

## ✅ Tamamlanma Kriterleri

- [ ] `api/database/` dizini oluşturuldu (5 dosya)
- [ ] SQLAlchemy models tanımlandı (5 tablo)
- [ ] CRUD operations implement edildi
- [ ] `api/main.py` lifespan ile database init
- [ ] `api/routes/factory.py` tamamen database kullanıyor
- [ ] In-memory `PROJECTS = {}` kaldırıldı
- [ ] `tests/conftest.py` test database fixture
- [ ] Mevcut 431 test geçiyor
- [ ] Server restart sonrası veriler kalıcı
- [ ] API response yapısı değişmedi (frontend uyumlu)
- [ ] `requirements.txt` güncellendi
- [ ] `git add -A && git commit && git push`

---

## 📊 Beklenen Sonuç

| Metrik | Önceki | Sonrası |
|--------|--------|---------|
| Storage | In-memory dict | SQLite database |
| Persistence | Server restart = veri kaybı | Kalıcı |
| Scalability | Tek process | Database-backed |
| AI caching | Yok | Interpretation persist |
| Analysis caching | Yok | Result persist |
