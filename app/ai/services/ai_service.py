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
from app.core.metrics import metrics


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

        metrics.total_requests += 1

        self._logger.info(
            "ai_request_started",
            model=request.model,
        )

        try:

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

                    self._logger.info(
                        "tool_called",
                        tool="calculator",
                    )

                    result = await tool.execute(
                        validated_request.user_prompt[5:].strip()
                    )

                    metrics.tool_calls += 1
                    metrics.successful_requests += 1

                    return AIResponse(
                        content=result,
                        provider="calculator",
                        model="tool",
                    )

            # -------------------------
            # DateTime Tool
            # -------------------------
            if (
                "current date" in prompt
                or "current time" in prompt
            ):

                tool = self._tools.get("datetime")

                if tool:

                    self._logger.info(
                        "tool_called",
                        tool="datetime",
                    )

                    result = await tool.execute("")

                    metrics.tool_calls += 1
                    metrics.successful_requests += 1

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
                            "Return ONLY valid JSON.\n\n"
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

                content = (
                    response.content
                    .replace("```json", "")
                    .replace("```JSON", "")
                    .replace("```", "")
                    .strip()
                )

                data = json.loads(content)

                structured = SummaryResponse(
                    **data
                )

                metrics.provider_calls += 1
                metrics.successful_requests += 1

                self._logger.info(
                    "ai_request_completed",
                    provider=response.provider,
                    model=response.model,
                )

                return AIResponse(
                    content=structured.model_dump_json(
                        indent=2
                    ),
                    provider=response.provider,
                    model=response.model,
                )

            # -------------------------
            # Standard LLM Request
            # -------------------------
            response = await self._gateway.generate(
                validated_request
            )

            validated_response = self._output_guard.validate(
                response
            )

            metrics.provider_calls += 1
            metrics.successful_requests += 1

            self._logger.info(
                "ai_request_completed",
                provider=validated_response.provider,
                model=validated_response.model,
            )

            return validated_response

        except Exception:

            metrics.failed_requests += 1

            raise