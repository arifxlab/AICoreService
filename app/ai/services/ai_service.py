"""
Business logic for AI interactions.
"""

from app.ai.gateway.base import AIGateway
from app.ai.guardrails import (
    InputGuardrail,
    OutputGuardrail,
)
from app.ai.schemas.ai import AIRequest, AIResponse
from app.core.logging import get_logger


class AIService:
    """
    Coordinates AI interactions.
    """

    def __init__(
        self,
        gateway: AIGateway,
    ) -> None:
        self._gateway = gateway

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

        validated_request = self._input_guard.validate(
            request
        )

        response = await self._gateway.generate(
            validated_request
        )

        validated_response = self._output_guard.validate(
            response
        )

        self._logger.info(
            "ai_request_completed",
            provider=validated_response.provider,
            model=validated_response.model,
        )

        return validated_response