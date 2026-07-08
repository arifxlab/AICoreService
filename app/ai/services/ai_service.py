"""
Business logic for AI interactions.
"""

from app.ai.providers.base import AIProvider
from app.ai.schemas.ai import AIRequest, AIResponse
from app.ai.guardrails import (
    InputGuardrail,
    OutputGuardrail,
)
from app.core.logging import get_logger


class AIService:
    """
    Coordinates AI interactions.
    """

    def __init__(
        self,
        provider: AIProvider,
    ) -> None:
        self._provider = provider

        self._input_guard = InputGuardrail()
        self._output_guard = OutputGuardrail()

        self._logger = get_logger()

    async def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Generate an AI response.
        """

        self._logger.info(
            "ai_request_started",
            model=request.model,
        )

        # Validate incoming request
        validated_request = self._input_guard.validate(
            request
        )

        # Call AI provider
        response = await self._provider.generate(
            validated_request
        )

        # Validate AI response
        validated_response = self._output_guard.validate(
            response
        )

        self._logger.info(
            "ai_request_completed",
            provider=response.provider,
            model=response.model,
        )

        return validated_response