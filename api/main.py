"""ExergyLab FastAPI Application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.analysis import router as analysis_router
from api.routes.benchmarks import router as benchmarks_router
from api.routes.chat import router as chat_router
from api.routes.factory import router as factory_router
from api.routes.interpret import router as interpret_router
from api.routes.solutions import router as solutions_router

app = FastAPI(
    title="ExergyLab API",
    description="Kompresör exergy analizi ve optimizasyon API'si",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(analysis_router, prefix="/api", tags=["analysis"])
app.include_router(benchmarks_router, prefix="/api", tags=["benchmarks"])
app.include_router(factory_router, prefix="/api", tags=["factory"])
app.include_router(interpret_router, prefix="/api", tags=["interpretation"])
app.include_router(solutions_router, prefix="/api", tags=["solutions"])
app.include_router(chat_router, prefix="/api", tags=["chat"])


@app.get("/")
async def root():
    return {
        "name": "ExergyLab API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health():
    return {"status": "ok"}
