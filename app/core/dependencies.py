"""
Application dependencies.
"""

from functools import lru_cache

from app.ai.gateway import DefaultAIGateway
from app.ai.gateway.base import AIGateway
from app.ai.providers.base import AIProvider
from app.ai.providers.factory import create_ai_provider
from app.ai.services.ai_service import AIService
from app.core.settings import get_settings


@lru_cache
def get_provider() -> AIProvider:
    """
    Return configured AI provider.
    """

    settings = get_settings()

    return create_ai_provider(
        settings
    )


@lru_cache
def get_gateway() -> AIGateway:
    """
    Return configured AI gateway.
    """

    return DefaultAIGateway(
        provider=get_provider()
    )


@lru_cache
def get_ai_service() -> AIService:
    """
    Return AI service instance.
    """

    return AIService(gateway=get_gateway())