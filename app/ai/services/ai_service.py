"""
Business logic for AI interactions.
"""

import json

from app.ai.gateway.base import AIGateway
from app.ai.guardrails import (
    InputGuardrail,
    OutputGuardrail,
)
from app.ai.schemas.ai import (
    AIRequest,
    AIResponse,
)
from app.ai.schemas.structured import SummaryResponse
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

        # -------------------------
        # Validate Request
        # -------------------------
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
        # Date & Time Tool
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
        # Structured Output
        # -------------------------
        if prompt.startswith("summarize:"):

            structured_request = validated_request.model_copy(
                update={
                    "user_prompt": (
                        "Return ONLY valid JSON using this schema:\n\n"
                        "{\n"
                        '  "summary": "...",\n'
                        '  "keywords": ["...", "..."]\n'
                        "}\n\n"
                        + validated_request.user_prompt[10:].strip()
                    )
                }
            )

            response = await self._gateway.generate(
                structured_request
            )

            # -------------------------
            # DEBUG
            # -------------------------
            print("\n========== RAW MODEL RESPONSE ==========")
            print("\n========== RAW MODEL RESPONSE ==========")
            print(response.content)
            print("========================================\n")

            content = response.content.strip()

            content = (
                content.replace("```json", "")
                .replace("```JSON", "")
                .replace("```", "")
                .strip()
            )

            print("\n========== CLEANED JSON ==========")
            print(content)
            print("=================================\n")

            data = json.loads(content)

            structured = SummaryResponse(
                **data
            )

            return AIResponse(
                content=structured.model_dump_json(
                    indent=2
                ),
                provider=response.provider,
                model=response.model,
            )

        # -------------------------
        # Normal LLM Request
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