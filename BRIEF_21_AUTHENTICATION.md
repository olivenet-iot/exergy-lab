# Brief 21: Authentication — JWT + User Ownership

> **Claude Code için:** Bu brief'i oku ve uygula. Basit JWT authentication ekle. Kullanıcılar kayıt olabilir, giriş yapabilir, ve sadece kendi projelerini görebilir.

---

## 🎯 Hedef

**Mevcut durum:** Herkes her şeyi görebilir. Auth yok.

**Hedef:** 
- Register/Login endpoints
- JWT token based auth
- Projeler kullanıcıya ait
- Protected routes

**Scope:** Backend auth + minimal frontend (login page). Karmaşık role-based access değil, basit user ownership.

---

## ⚠️ OTONOM YETKİ

1. Brief'teki görevleri tamamla
2. Mevcut API endpoint'lerinin çalışmasını BOZMA
3. 431 testi BOZMA (auth opsiyonel olacak testlerde)
4. `python-jose` ve `passlib` dışında yeni paket EKLEME
5. Frontend'de sadece login sayfası ekle

---

## 📋 Adım 0: Mevcut Durumu Anla

```bash
# 1. Database models — User eklenecek
cat api/database/models.py

# 2. Factory routes — user_id eklenecek
cat api/routes/factory.py

# 3. Main app
cat api/main.py

# 4. Mevcut schemas
ls api/schemas/

# 5. Frontend App.jsx — routing
cat frontend/src/App.jsx

# 6. Frontend api service
cat frontend/src/services/api.js
```

---

## 🗄️ Database Güncellemesi

### Yeni Model: User

```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(String(36), primary_key=True, default=generate_uuid)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    projects = relationship("FactoryProject", back_populates="owner", cascade="all, delete-orphan")
```

### FactoryProject Güncellemesi

```python
class FactoryProject(Base):
    # ... mevcut alanlar ...
    
    # YENİ: Owner ilişkisi
    owner_id = Column(String(36), ForeignKey("users.id"), nullable=True)  # nullable for migration
    owner = relationship("User", back_populates="projects")
```

---

## 📦 Dosya Yapısı

```
api/
├── auth/                        # YENİ dizin
│   ├── __init__.py
│   ├── config.py               # JWT settings
│   ├── security.py             # Password hashing, JWT creation
│   ├── dependencies.py         # get_current_user dependency
│   └── schemas.py              # Auth request/response schemas
├── routes/
│   ├── auth.py                 # YENİ: Register/Login endpoints
│   └── factory.py              # GÜNCELLEME: user ownership
├── database/
│   ├── models.py               # GÜNCELLEME: User model
│   └── crud.py                 # GÜNCELLEME: User CRUD
└── main.py                     # GÜNCELLEME: Auth router mount
```

---

## 📦 Adım 1: Dependencies

### `requirements.txt` — Eklemeler

```
# Auth
python-jose[cryptography]>=3.3.0
passlib[bcrypt]>=1.7.4
```

---

## 📦 Adım 2: Auth Configuration

### `api/auth/config.py`

```python
"""
JWT and auth configuration.
"""
import os
from datetime import timedelta

# JWT Settings
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "exergylab-dev-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
```

---

## 📦 Adım 3: Security Utilities

### `api/auth/security.py`

```python
"""
Password hashing and JWT token utilities.
"""
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from passlib.context import CryptContext

from api.auth.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> Optional[dict]:
    """Decode and verify a JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
```

---

## 📦 Adım 4: Auth Schemas

### `api/auth/schemas.py`

```python
"""
Authentication request/response schemas.
"""
from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    """Registration request."""
    email: EmailStr
    password: str = Field(..., min_length=6)
    full_name: str = Field(None, max_length=255)


class UserLogin(BaseModel):
    """Login request."""
    email: EmailStr
    password: str


class Token(BaseModel):
    """Token response."""
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    """User info response."""
    id: str
    email: str
    full_name: str | None
    is_active: bool
```

---

## 📦 Adım 5: Auth Dependencies

### `api/auth/dependencies.py`

```python
"""
Authentication dependencies for FastAPI.
"""
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from api.database.session import get_db
from api.database import crud
from api.auth.security import decode_token

# Bearer token scheme
security = HTTPBearer(auto_error=False)


async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """
    Get current authenticated user.
    Returns None if no valid token (allows optional auth).
    """
    if not credentials:
        return None
    
    token = credentials.credentials
    payload = decode_token(token)
    
    if not payload:
        return None
    
    user_id = payload.get("sub")
    if not user_id:
        return None
    
    user = await crud.get_user(db, user_id)
    return user


async def require_auth(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    db: AsyncSession = Depends(get_db)
):
    """
    Require authentication. Raises 401 if not authenticated.
    """
    token = credentials.credentials
    payload = decode_token(token)
    
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )
    
    user = await crud.get_user(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is inactive",
        )
    
    return user
```

---

## 📦 Adım 6: Auth Routes

### `api/routes/auth.py`

```python
"""
Authentication routes: register, login, me.
"""
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.database.session import get_db
from api.database import crud
from api.auth.schemas import UserRegister, UserLogin, Token, UserResponse
from api.auth.security import verify_password, get_password_hash, create_access_token
from api.auth.dependencies import require_auth

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserRegister, db: AsyncSession = Depends(get_db)):
    """Register a new user."""
    # Check if email exists
    existing = await crud.get_user_by_email(db, user_data.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create user
    hashed_password = get_password_hash(user_data.password)
    user = await crud.create_user(
        db,
        email=user_data.email,
        hashed_password=hashed_password,
        full_name=user_data.full_name
    )
    
    return UserResponse(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        is_active=user.is_active
    )


@router.post("/login", response_model=Token)
async def login(credentials: UserLogin, db: AsyncSession = Depends(get_db)):
    """Login and get access token."""
    user = await crud.get_user_by_email(db, credentials.email)
    
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is inactive"
        )
    
    # Create token
    access_token = create_access_token(data={"sub": user.id})
    
    return Token(access_token=access_token)


@router.get("/me", response_model=UserResponse)
async def get_me(user = Depends(require_auth)):
    """Get current user info."""
    return UserResponse(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        is_active=user.is_active
    )
```

---

## 📦 Adım 7: Database Updates

### `api/database/models.py` — User Model Ekleme

```python
# Mevcut import'lara ekle:
from sqlalchemy import Boolean

# Yeni model ekle (FactoryProject'ten ÖNCE):
class User(Base):
    __tablename__ = "users"
    
    id = Column(String(36), primary_key=True, default=generate_uuid)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    projects = relationship("FactoryProject", back_populates="owner")


# FactoryProject'a ekle:
class FactoryProject(Base):
    # ... mevcut alanlar ...
    
    # YENİ alan:
    owner_id = Column(String(36), ForeignKey("users.id"), nullable=True)
    
    # YENİ relationship:
    owner = relationship("User", back_populates="projects")
```

### `api/database/crud.py` — User CRUD Ekleme

```python
# Yeni fonksiyonlar ekle:

async def create_user(
    db: AsyncSession,
    email: str,
    hashed_password: str,
    full_name: Optional[str] = None
) -> "User":
    """Create a new user."""
    from api.database.models import User
    user = User(
        email=email,
        hashed_password=hashed_password,
        full_name=full_name
    )
    db.add(user)
    await db.flush()
    await db.refresh(user)
    return user


async def get_user(db: AsyncSession, user_id: str) -> Optional["User"]:
    """Get user by ID."""
    from api.database.models import User
    result = await db.execute(
        select(User).where(User.id == user_id)
    )
    return result.scalar_one_or_none()


async def get_user_by_email(db: AsyncSession, email: str) -> Optional["User"]:
    """Get user by email."""
    from api.database.models import User
    result = await db.execute(
        select(User).where(User.email == email)
    )
    return result.scalar_one_or_none()
```

### `api/database/crud.py` — Project CRUD Güncelleme

```python
# create_project'a owner_id ekle:
async def create_project(
    db: AsyncSession,
    name: str,
    sector: Optional[str] = None,
    description: Optional[str] = None,
    owner_id: Optional[str] = None  # YENİ
) -> FactoryProject:
    """Create a new factory project."""
    project = FactoryProject(
        name=name,
        sector=sector,
        description=description,
        owner_id=owner_id  # YENİ
    )
    # ... rest same


# get_all_projects'a owner filter ekle:
async def get_all_projects(
    db: AsyncSession,
    owner_id: Optional[str] = None  # YENİ
) -> List[FactoryProject]:
    """Get all projects, optionally filtered by owner."""
    query = select(FactoryProject).options(
        selectinload(FactoryProject.equipment)
    )
    if owner_id:
        query = query.where(FactoryProject.owner_id == owner_id)
    query = query.order_by(FactoryProject.created_at.desc())
    result = await db.execute(query)
    return list(result.scalars().all())
```

---

## 📦 Adım 8: Factory Routes Update

### `api/routes/factory.py` — Owner Integration

```python
# Import ekle:
from api.auth.dependencies import get_current_user

# create_project güncelle:
@router.post("/projects", response_model=FactoryProjectResponse)
async def create_project(
    project: FactoryProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)  # YENİ
):
    """Create a new factory project."""
    owner_id = current_user.id if current_user else None
    db_project = await crud.create_project(
        db,
        name=project.name,
        sector=project.sector,
        description=project.description,
        owner_id=owner_id  # YENİ
    )
    return _format_project(db_project)


# list_projects güncelle:
@router.get("/projects", response_model=list[FactoryProjectResponse])
async def list_projects(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)  # YENİ
):
    """List factory projects. If authenticated, shows only user's projects."""
    owner_id = current_user.id if current_user else None
    projects = await crud.get_all_projects(db, owner_id=owner_id)
    return [_format_project(p) for p in projects]


# get_project güncelle — ownership check:
@router.get("/projects/{project_id}", response_model=FactoryProjectResponse)
async def get_project(
    project_id: str,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get a factory project by ID."""
    project = await crud.get_project(db, project_id)
    if not project:
        raise HTTPException(404, "Project not found")
    
    # Ownership check (if authenticated)
    if current_user and project.owner_id and project.owner_id != current_user.id:
        raise HTTPException(403, "Not authorized to access this project")
    
    return _format_project(project)


# Diğer endpoint'lere de benzer ownership check ekle
```

---

## 📦 Adım 9: Main App Update

### `api/main.py` — Auth Router Mount

```python
# Import ekle:
from api.routes.auth import router as auth_router

# Router mount (diğer router'larla birlikte):
app.include_router(auth_router, prefix="/api")
```

---

## 📦 Adım 10: Frontend — Login Page (Minimal)

### `frontend/src/pages/Login.jsx`

```jsx
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { login, register } from '../services/api';

export default function Login() {
  const [isRegister, setIsRegister] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      if (isRegister) {
        await register({ email, password, full_name: fullName });
      }
      const { access_token } = await login({ email, password });
      localStorage.setItem('token', access_token);
      navigate('/factory');
    } catch (err) {
      setError(err.response?.data?.detail || 'Bir hata oluştu');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold text-center mb-6">
          {isRegister ? 'Kayıt Ol' : 'Giriş Yap'}
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">
          {isRegister && (
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">
                Ad Soyad
              </label>
              <input
                type="text"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-cyan-500"
              />
            </div>
          )}

          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1">
              E-posta
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-cyan-500"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1">
              Şifre
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              minLength={6}
              className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-cyan-500"
            />
          </div>

          {error && (
            <div className="text-red-600 text-sm">{error}</div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full py-2 bg-cyan-600 text-white rounded-lg hover:bg-cyan-700 disabled:opacity-50"
          >
            {loading ? '...' : isRegister ? 'Kayıt Ol' : 'Giriş Yap'}
          </button>
        </form>

        <p className="text-center mt-4 text-sm text-slate-600">
          {isRegister ? 'Zaten hesabın var mı?' : 'Hesabın yok mu?'}{' '}
          <button
            onClick={() => setIsRegister(!isRegister)}
            className="text-cyan-600 hover:underline"
          >
            {isRegister ? 'Giriş Yap' : 'Kayıt Ol'}
          </button>
        </p>
      </div>
    </div>
  );
}
```

### `frontend/src/services/api.js` — Auth Functions

```javascript
// Mevcut api instance'a interceptor ekle:
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth fonksiyonları:
export const register = async (data) => {
  const response = await api.post('/auth/register', data);
  return response.data;
};

export const login = async (data) => {
  const response = await api.post('/auth/login', data);
  return response.data;
};

export const getMe = async () => {
  const response = await api.get('/auth/me');
  return response.data;
};

export const logout = () => {
  localStorage.removeItem('token');
};
```

### `frontend/src/App.jsx` — Route Ekleme

```jsx
// Import:
import Login from './pages/Login';

// Route ekle:
<Route path="/login" element={<Login />} />
```

---

## 📦 Adım 11: Header'a Login/Logout

### `frontend/src/components/layout/Header.jsx` — User Menu

```jsx
// Basit user indicator + logout butonu
// Token varsa: "Hoşgeldin" + Logout
// Token yoksa: "Giriş Yap" linki
```

---

## 📋 Uygulama Sırası

### Faz 1: Dependencies
1. `requirements.txt` — python-jose, passlib ekle
2. `pip install python-jose[cryptography] passlib[bcrypt]`

### Faz 2: Auth Backend
3. `api/auth/` dizini oluştur
4. `api/auth/__init__.py`
5. `api/auth/config.py`
6. `api/auth/security.py`
7. `api/auth/schemas.py`
8. `api/auth/dependencies.py`
9. `api/routes/auth.py`

### Faz 3: Database Updates
10. `api/database/models.py` — User model + FactoryProject.owner_id
11. `api/database/crud.py` — User CRUD + owner filter

### Faz 4: Integration
12. `api/main.py` — Auth router mount
13. `api/routes/factory.py` — Ownership integration

### Faz 5: Frontend
14. `frontend/src/services/api.js` — Auth functions + interceptor
15. `frontend/src/pages/Login.jsx`
16. `frontend/src/App.jsx` — Login route
17. `frontend/src/components/layout/Header.jsx` — User menu

### Faz 6: Verification
18. `pytest tests/ -v` — 431 test geçmeli
19. `cd frontend && npx vite build`
20. Manual test: register → login → create project → logout → login → see only own projects
21. `git add -A && git commit && git push`

---

## ⚠️ Önemli Notlar

1. **Auth opsiyonel.** `get_current_user` None dönebilir. Bu sayede mevcut testler bozulmaz.

2. **Backward compatibility.** Eski projeler (owner_id=None) herkes tarafından görülebilir.

3. **Token storage.** localStorage kullanıyoruz (basit). Production'da httpOnly cookie daha güvenli.

4. **Password validation.** Minimum 6 karakter. Daha sıkı kurallar eklenebilir.

5. **No email verification.** MVP için yok. Sonra eklenebilir.

---

## ✅ Tamamlanma Kriterleri

- [ ] `api/auth/` dizini oluşturuldu (5 dosya)
- [ ] User model eklendi
- [ ] FactoryProject.owner_id eklendi
- [ ] Register/Login/Me endpoints çalışıyor
- [ ] JWT token oluşturma ve doğrulama
- [ ] Factory routes ownership integration
- [ ] Frontend login sayfası
- [ ] API interceptor ile token gönderme
- [ ] Header'da user menu
- [ ] 431 test geçiyor
- [ ] Manual test: register → login → create → logout → login → see own
- [ ] `git add -A && git commit && git push`
