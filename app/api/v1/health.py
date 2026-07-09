"""
Health check endpoint.
"""

from fastapi import APIRouter

from app.core.settings import get_settings

settings = get_settings()

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "",
    summary="Health Check",
    description="Returns the current status of the AI Core Service.",
)
async def health() -> dict[str, str]:
    """
    Return the application's health status.
    """

    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }