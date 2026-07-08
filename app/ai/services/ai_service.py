"""
Business logic for AI interactions.
"""

from app.ai.providers.base import AIProvider
from app.ai.schemas.ai import AIRequest, AIResponse


class AIService:
    """
    Coordinates AI interactions.
    """

    def __init__(self, provider: AIProvider) -> None:
        self._provider = provider

    async def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Generate an AI response using the configured provider.
        """
        return await self._provider.generate(request)