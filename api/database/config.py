"""Database configuration for ExergyLab."""

import os

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "sqlite+aiosqlite:///./exergylab.db",
)
