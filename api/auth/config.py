"""JWT configuration for ExergyLab authentication."""

import os

SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "exergylab-dev-secret-key-change-in-production",
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
