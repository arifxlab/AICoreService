"""
OpenRouter AI provider implementation.
"""

from typing import Any

import httpx

from app.ai.providers.base import AIProvider
from app.ai.schemas.ai import AIRequest, AIResponse
from app.core.exceptions import AIProviderError
from app.core.logging import get_logger


class OpenRouterProvider(AIProvider):
    """
    AI provider implementation that communicates with
    the OpenRouter Chat Completions API.
    """

    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
    REFERER = "http://localhost:8000"
    APP_NAME = "AI Core Service"

    def __init__(
        self,
        api_key: str,
        model: str,
        temperature: float,
        max_tokens: int,
    ) -> None:
        self._api_key = api_key
        self._model = model
        self._temperature = temperature
        self._max_tokens = max_tokens

        self._logger = get_logger()

        self._client = httpx.AsyncClient(
            timeout=30.0,
        )

    async def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Send a completion request to OpenRouter and
        return a normalized AIResponse.
        """

        payload: dict[str, Any] = {
            "model": self._model,
            "temperature": self._temperature,
            "max_tokens": self._max_tokens,
            "messages": [
                {
                    "role": "system",
                    "content": request.system_prompt,
                },
                {
                    "role": "user",
                    "content": request.user_prompt,
                },
            ],
        }

        # -------------------------------------------------
        # Future Tool Support
        # -------------------------------------------------
        if request.tool_schema:
            payload["tools"] = request.tool_schema

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": self.REFERER,
            "X-Title": self.APP_NAME,
        }

        response = await self._client.post(
            self.BASE_URL,
            json=payload,
            headers=headers,
        )

        if response.status_code != 200:
            self._logger.error(
                "openrouter_request_failed",
                status_code=response.status_code,
                response=response.text,
            )

        try:
            response.raise_for_status()

        except httpx.HTTPStatusError as exc:
            raise AIProviderError(
                message=(
                    f"OpenRouter request failed " f"(HTTP {response.status_code})."
                ),
                provider="openrouter",
            ) from exc

        data = response.json()

        choices = data.get("choices", [])

        if not choices:
            raise AIProviderError(
                message="OpenRouter returned no choices.",
                provider="openrouter",
            )

        message = choices[0].get("message", {})

        content = message.get("content", "")

        stop_reason = choices[0].get(
            "finish_reason",
        )

        return AIResponse(
            content=content,
            provider="openrouter",
            model=self._model,
            stop_reason=stop_reason,
        )

    async def close(self) -> None:
        """
        Close the underlying HTTP client.
        """

        await self._client.aclose()
