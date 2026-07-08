"""
AI Gateway interface.
"""

from abc import ABC, abstractmethod

from app.ai.schemas.ai import AIRequest, AIResponse


class AIGateway(ABC):
    """
    Abstract AI gateway contract.
    """

    @abstractmethod
    async def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Generate AI response through gateway.
        """

        pass