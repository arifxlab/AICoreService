"""
Application entry point.
"""

from fastapi import FastAPI

from app.api.routes import api_router
from app.core.exceptions import AIProviderError
from app.core.handlers import ai_provider_exception_handler
from app.core.logging import configure_logging
from app.core.settings import get_settings


configure_logging()

settings = get_settings()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)


# Exception handlers
app.add_exception_handler(
    AIProviderError,
    ai_provider_exception_handler,
)


# API Routes
app.include_router(
    api_router,
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