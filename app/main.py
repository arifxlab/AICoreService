"""
Application entry point.
"""

from fastapi import FastAPI

from app.core.logging import configure_logging
from app.api.routes import router
from app.core.settings import get_settings

configure_logging()

settings = get_settings()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)


app.include_router(
    router,
    prefix="/api",
)


@app.get("/")
async def root() -> dict[str, str]:
    """
    Root endpoint.
    """
    return {
        "message": f"Welcome to {settings.app_name}",
    }


@app.get("/health")
async def health() -> dict[str, str]:
    """
    Health check endpoint.
    """
    return {
        "status": "healthy",
        "environment": settings.environment,
        "version": settings.app_version,
    }