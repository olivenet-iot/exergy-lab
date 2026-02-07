"""SQLAlchemy 2.0 models for ExergyLab."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, JSON, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


def _short_uuid() -> str:
    return str(uuid.uuid4())[:8]


def _full_uuid() -> str:
    return str(uuid.uuid4())


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_full_uuid)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    projects: Mapped[list["FactoryProject"]] = relationship(
        back_populates="owner",
        lazy="raise",
    )


class FactoryProject(Base):
    __tablename__ = "factory_projects"

    id: Mapped[str] = mapped_column(String(8), primary_key=True, default=_short_uuid)
    name: Mapped[str] = mapped_column(String(255))
    sector: Mapped[str | None] = mapped_column(String(50), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    owner_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("users.id"), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, onupdate=_utcnow)

    # Process definition fields (gap analysis)
    process_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    process_label: Mapped[str | None] = mapped_column(String(255), nullable=True)
    process_parameters: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    process_subcategory: Mapped[str | None] = mapped_column(String(50), nullable=True)
    operating_hours: Mapped[float | None] = mapped_column(Float, nullable=True)
    energy_price_eur_kwh: Mapped[float | None] = mapped_column(Float, nullable=True)

    owner: Mapped["User | None"] = relationship(back_populates="projects")
    equipment: Mapped[list["Equipment"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
        lazy="raise",
    )
    factory_analyses: Mapped[list["FactoryAnalysis"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
        lazy="raise",
    )
    ai_interpretations: Mapped[list["AIInterpretation"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
        lazy="raise",
    )


class Equipment(Base):
    __tablename__ = "equipment"

    id: Mapped[str] = mapped_column(String(8), primary_key=True, default=_short_uuid)
    project_id: Mapped[str] = mapped_column(
        String(8), ForeignKey("factory_projects.id", ondelete="CASCADE")
    )
    name: Mapped[str] = mapped_column(String(255))
    equipment_type: Mapped[str] = mapped_column(String(50))
    subtype: Mapped[str | None] = mapped_column(String(50), nullable=True)
    parameters: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    project: Mapped["FactoryProject"] = relationship(back_populates="equipment")
    analysis_result: Mapped["AnalysisResult | None"] = relationship(
        back_populates="equipment",
        uselist=False,
        cascade="all, delete-orphan",
        lazy="raise",
    )


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id: Mapped[str] = mapped_column(String(8), primary_key=True, default=_short_uuid)
    equipment_id: Mapped[str] = mapped_column(
        String(8),
        ForeignKey("equipment.id", ondelete="CASCADE"),
        unique=True,
    )
    result_data: Mapped[dict] = mapped_column(JSON)
    analyzed_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    equipment: Mapped["Equipment"] = relationship(back_populates="analysis_result")


class FactoryAnalysis(Base):
    __tablename__ = "factory_analyses"

    id: Mapped[str] = mapped_column(String(8), primary_key=True, default=_short_uuid)
    project_id: Mapped[str] = mapped_column(
        String(8), ForeignKey("factory_projects.id", ondelete="CASCADE")
    )
    aggregates: Mapped[dict] = mapped_column(JSON)
    hotspots: Mapped[dict] = mapped_column(JSON)
    integration_opportunities: Mapped[dict] = mapped_column(JSON)
    sankey_data: Mapped[dict] = mapped_column(JSON)
    gap_analysis: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    analyzed_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    project: Mapped["FactoryProject"] = relationship(back_populates="factory_analyses")


class AIInterpretation(Base):
    __tablename__ = "ai_interpretations"

    id: Mapped[str] = mapped_column(String(8), primary_key=True, default=_short_uuid)
    project_id: Mapped[str | None] = mapped_column(
        String(8),
        ForeignKey("factory_projects.id", ondelete="CASCADE"),
        nullable=True,
    )
    equipment_id: Mapped[str | None] = mapped_column(
        String(8),
        ForeignKey("equipment.id", ondelete="CASCADE"),
        nullable=True,
    )
    interpretation_data: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    project: Mapped["FactoryProject | None"] = relationship(
        back_populates="ai_interpretations"
    )
