"""
Application entry point.
"""

from fastapi import FastAPI

from app.api.routes import api_router
from app.core.exceptions import AIProviderError
from app.core.handlers import ai_provider_exception_handler
from app.core.logging import configure_logging
from app.core.settings import get_settings

# Configure application logging.
configure_logging()

# Load application settings.
settings = get_settings()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    description=(
        "AI Core Service providing LLM access, "
        "tool execution, and structured AI responses."
    ),
    openapi_tags=[
        {"name": "Chat", "description": "AI chat endpoints"},
        {"name": "Health", "description": "Health check endpoint"},
        {"name": "Metrics", "description": "Application metrics"},
    ],
)


# Register exception handlers.
app.add_exception_handler(
    AIProviderError,
    ai_provider_exception_handler,
)


# Register API routes.
app.include_router(api_router)


@app.get("/")
async def root() -> dict[str, str]:
    """
    Root endpoint.
    """

    return {
        "message": f"{settings.app_name} is running successfully."
    }