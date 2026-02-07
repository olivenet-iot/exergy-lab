"""Async database session management for ExergyLab."""

import logging
from collections.abc import AsyncGenerator

from sqlalchemy import inspect, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from api.database.config import DATABASE_URL
from api.database.models import Base

logger = logging.getLogger(__name__)

engine = create_async_engine(DATABASE_URL, echo=False)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Column migrations for existing tables (table_name -> [(column_name, sql_type)])
_MIGRATIONS = {
    "factory_projects": [
        ("process_type", "VARCHAR(50)"),
        ("process_label", "VARCHAR(255)"),
        ("process_parameters", "JSON"),
        ("process_subcategory", "VARCHAR(50)"),
        ("operating_hours", "FLOAT"),
        ("energy_price_eur_kwh", "FLOAT"),
    ],
    "factory_analyses": [
        ("gap_analysis", "JSON"),
    ],
}


def _migrate_columns(connection):
    """Add missing columns to existing tables (SQLite compatible)."""
    insp = inspect(connection)
    for table_name, columns in _MIGRATIONS.items():
        if not insp.has_table(table_name):
            continue
        existing = {col["name"] for col in insp.get_columns(table_name)}
        for col_name, col_type in columns:
            if col_name not in existing:
                connection.execute(
                    text(f"ALTER TABLE {table_name} ADD COLUMN {col_name} {col_type}")
                )
                logger.info("Added column %s.%s", table_name, col_name)


async def init_db() -> None:
    """Create all tables and run migrations for new columns."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.run_sync(_migrate_columns)


async def close_db() -> None:
    """Dispose of the engine."""
    await engine.dispose()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI dependency that yields an async session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
