"""
AI gateway interface.
"""

from abc import ABC, abstractmethod

from app.ai.schemas.ai import AIRequest, AIResponse


class AIGateway(ABC):
    """
    Abstract interface for AI gateway implementations.

    Gateway implementations are responsible for routing AI requests
    to the configured provider and returning standardized responses.
    """

    @abstractmethod
    async def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Generate an AI response for the given request.

        Args:
            request: The validated AI request.

        Returns:
            A standardized AI response.
        """
        ...