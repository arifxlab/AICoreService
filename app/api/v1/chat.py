"""
Chat API endpoints.
"""

from fastapi import APIRouter, Depends

from app.ai.schemas.ai import AIRequest, AIResponse
from app.ai.services.ai_service import AIService
from app.core.dependencies import get_ai_service


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=AIResponse,
)
async def chat(
    request: AIRequest,
    service: AIService = Depends(get_ai_service),
) -> AIResponse:
    """
    Generate an AI response.
    """

    return await service.generate(request)