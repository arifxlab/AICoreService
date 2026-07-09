"""
Application dependency providers.
"""

from functools import lru_cache

from app.ai.gateway import DefaultAIGateway
from app.ai.gateway.base import AIGateway
from app.ai.providers.base import AIProvider
from app.ai.providers.factory import create_ai_provider
from app.ai.services.ai_service import AIService
from app.ai.tools.registry import ToolRegistry
from app.core.settings import get_settings


@lru_cache
def get_provider() -> AIProvider:
    """
    Return the configured AI provider instance.

    The provider is cached to ensure a single shared instance
    throughout the application's lifetime.
    """

    settings = get_settings()

    return create_ai_provider(settings)


@lru_cache
def get_gateway() -> AIGateway:
    """
    Return the application's AI gateway.

    The gateway coordinates communication between the service
    layer and the configured AI provider.
    """

    return DefaultAIGateway(
        provider=get_provider(),
    )


@lru_cache
def get_tool_registry() -> ToolRegistry:
    """
    Return the application's tool registry.

    The registry maintains all available AI tools and is shared
    across the application.
    """

    return ToolRegistry()


@lru_cache
def get_ai_service() -> AIService:
    """
    Return the application's AI service.

    The service orchestrates guardrails, tools, and the AI gateway.
    A cached instance is used to avoid recreating dependencies
    for every request.
    """

    return AIService(
        gateway=get_gateway(),
        tool_registry=get_tool_registry(),
    )
