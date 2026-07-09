"""
Central API router registration.
"""

from fastapi import APIRouter

from app.api.v1.chat import router as chat_router
from app.api.v1.health import router as health_router
from app.api.v1.metrics import router as metrics_router

api_router = APIRouter()


# Versioned API endpoints
api_router.include_router(
    chat_router,
    prefix="/api/v1",
)

# System endpoints
api_router.include_router(
    health_router,
)

api_router.include_router(
    metrics_router,
)
