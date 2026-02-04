"""Test configuration for ExergyLab."""

import asyncio
import sys
import os

# Ensure project root is on sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from sqlalchemy import StaticPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from api.database.models import Base
from api.database.session import get_db
from api.main import app

# ---------------------------------------------------------------------------
# Test database setup — module-level so overrides are in place before
# any test file creates its TestClient(app).
# ---------------------------------------------------------------------------

_test_engine = create_async_engine(
    "sqlite+aiosqlite:///:memory:",
    poolclass=StaticPool,
    connect_args={"check_same_thread": False},
)

_TestSessionLocal = async_sessionmaker(
    _test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def _override_get_db():
    async with _TestSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


app.dependency_overrides[get_db] = _override_get_db


# ---------------------------------------------------------------------------
# Per-test fixture: create tables before, drop after each test.
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def _setup_test_db():
    """Create and drop all tables around each test for isolation."""
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(_create_tables())
        yield
        loop.run_until_complete(_drop_tables())
    finally:
        loop.close()


async def _create_tables():
    async with _test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def _drop_tables():
    async with _test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
