"""
Provider interface for AI models.
"""

from typing import Protocol

from app.ai.schemas.ai import AIRequest, AIResponse


class AIProvider(Protocol):
    """
    Contract every AI provider must implement.
    """

    async def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Generate a response from an AI model.
        """
        ...