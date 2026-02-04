"""Authentication routes for ExergyLab API."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.dependencies import require_auth
from api.auth.schemas import Token, UserLogin, UserRegister, UserResponse
from api.auth.security import create_access_token, get_password_hash, verify_password
from api.database import crud
from api.database.models import User
from api.database.session import get_db

router = APIRouter()


@router.post("/auth/register", response_model=UserResponse, status_code=201)
async def register(request: UserRegister, db: AsyncSession = Depends(get_db)):
    """Register a new user."""
    existing = await crud.get_user_by_email(db, request.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(request.password)
    user = await crud.create_user(
        db,
        email=request.email,
        hashed_password=hashed_password,
        full_name=request.full_name,
    )
    return UserResponse(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        is_active=user.is_active,
    )


@router.post("/auth/login", response_model=Token)
async def login(request: UserLogin, db: AsyncSession = Depends(get_db)):
    """Authenticate and return a JWT token."""
    user = await crud.get_user_by_email(db, request.email)
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is disabled")

    access_token = create_access_token(data={"sub": user.id})
    return Token(access_token=access_token)


@router.get("/auth/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(require_auth)):
    """Return current authenticated user info."""
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        full_name=current_user.full_name,
        is_active=current_user.is_active,
    )
