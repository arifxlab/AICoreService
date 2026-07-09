"""
Default AI gateway implementation.
"""

from time import perf_counter

from app.ai.gateway.base import AIGateway
from app.ai.providers.base import AIProvider
from app.ai.schemas.ai import AIRequest, AIResponse
from app.core.logging import get_logger
from app.core.metrics import metrics


class DefaultAIGateway(AIGateway):
    """
    Routes AI requests to the configured provider while
    collecting latency metrics and logging execution details.
    """

    def __init__(
        self,
        provider: AIProvider,
    ) -> None:
        self._logger = get_logger()
        self._provider = provider

    async def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Forward a request to the configured AI provider.
        """

        start = perf_counter()

        self._logger.info(
            "gateway_request_started",
            provider=self._provider.__class__.__name__,
        )

        try:
            response = await self._provider.generate(
                request
            )

            return response

        finally:
            latency_ms = round(
                (perf_counter() - start) * 1000,
                2,
            )

            metrics.total_latency_ms += latency_ms

            self._logger.info(
                "gateway_request_completed",
                provider=self._provider.__class__.__name__,
                latency_ms=latency_ms,
            )