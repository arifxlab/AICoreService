"""
Default AI gateway implementation.
"""

from time import perf_counter

from app.ai.gateway.base import AIGateway
from app.ai.providers.base import AIProvider
from app.ai.schemas.ai import AIRequest, AIResponse
from app.core.logging import get_logger


class DefaultAIGateway(AIGateway):
    """
    Gateway responsible for AI request routing.
    """

    def __init__(
        self,
        provider: AIProvider,
    ) -> None:
        self._provider = provider
        self._logger = get_logger()

    async def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Forward request to configured provider.
        """

        start = perf_counter()

        self._logger.info(
            "gateway_request_started",
            provider=self._provider.__class__.__name__,
        )

        response = await self._provider.generate(
            request
        )

        latency_ms = round(
            (perf_counter() - start) * 1000,
            2,
        )

        self._logger.info(
            "gateway_request_completed",
            provider=response.provider,
            model=response.model,
            latency_ms=latency_ms,
        )

        return response