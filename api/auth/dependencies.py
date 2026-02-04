"""FastAPI authentication dependencies."""

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.security import decode_token
from api.database.models import User
from api.database.session import get_db

# auto_error=False: returns None when no Authorization header is present
_optional_bearer = HTTPBearer(auto_error=False)

# auto_error=True: raises 401 automatically when no header is present
_required_bearer = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(_optional_bearer),
    db: AsyncSession = Depends(get_db),
) -> User | None:
    """Return the current user or None if no valid token.

    This is the KEY dependency for backward compatibility: endpoints that use
    this will continue to work without any Authorization header.
    """
    if credentials is None:
        return None

    payload = decode_token(credentials.credentials)
    if payload is None:
        return None

    user_id: str | None = payload.get("sub")
    if user_id is None:
        return None

    from api.database.crud import get_user

    user = await get_user(db, user_id)
    return user


async def require_auth(
    credentials: HTTPAuthorizationCredentials = Depends(_required_bearer),
    db: AsyncSession = Depends(get_db),
) -> User:
    """Return the current user or raise 401.

    Used on auth-specific endpoints like /auth/me.
    """
    payload = decode_token(credentials.credentials)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_id: str | None = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    from api.database.crud import get_user

    user = await get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user
