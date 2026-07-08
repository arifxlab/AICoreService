"""
Business logic for AI interactions.
"""

from app.ai.gateway.base import AIGateway
from app.ai.guardrails import (
    InputGuardrail,
    OutputGuardrail,
)
from app.ai.schemas.ai import AIRequest, AIResponse
from app.ai.tools.registry import ToolRegistry
from app.core.logging import get_logger


class AIService:
    """
    Coordinates AI interactions.
    """

    def __init__(
        self,
        gateway: AIGateway,
        tool_registry: ToolRegistry,
    ) -> None:
        self._gateway = gateway
        self._tools = tool_registry

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

        # Validate request
        validated_request = self._input_guard.validate(
            request
        )

        prompt = validated_request.user_prompt.lower()

        # -------------------------
        # Calculator Tool
        # -------------------------
        if prompt.startswith("calc:"):
            tool = self._tools.get("calculator")

            if tool:
                result = await tool.execute(
                    validated_request.user_prompt[5:].strip()
                )

                return AIResponse(
                    content=result,
                    provider="calculator",
                    model="tool",
                )

        # -------------------------
        # DateTime Tool
        # -------------------------
        if (
            "current time" in prompt
            or "current date" in prompt
        ):
            tool = self._tools.get("datetime")

            if tool:
                result = await tool.execute("")

                return AIResponse(
                    content=result,
                    provider="datetime",
                    model="tool",
                )

        # -------------------------
        # Gateway (LLM)
        # -------------------------
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