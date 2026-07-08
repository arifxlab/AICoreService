"""
OpenRouter AI provider implementation.
"""

from typing import Any

import httpx

from app.ai.providers.base import AIProvider
from app.ai.schemas.ai import AIRequest, AIResponse

from app.core.exceptions import AIProviderError

class OpenRouterProvider(AIProvider):
    """
    AI provider using OpenRouter API.
    """

    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

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


        self._client = httpx.AsyncClient(
            timeout=30.0,
        )

    async def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Send request to OpenRouter and return response.
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

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "AI Core Service",
        }

        response = await self._client.post(
            self.BASE_URL,
            json=payload,
            headers=headers,
        )

        if response.status_code != 200:
            print(
                "OpenRouter Status:",
                response.status_code,
            )

            print(
                "OpenRouter Response:",
                response.text,
            )

        try:
            response.raise_for_status()

        except httpx.HTTPStatusError as exc:
            raise AIProviderError(
                message="OpenRouter request failed.",
                provider="openrouter",
            ) from exc

        data = response.json()

        content = data["choices"][0]["message"]["content"]

        return AIResponse(
            content=content,
            provider="openrouter",
            model=self._model,
            stop_reason=None,
        )