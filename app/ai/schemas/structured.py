"""
Structured AI response schemas.
"""

from pydantic import BaseModel


class SummaryResponse(BaseModel):
    """
    Structured summary response.
    """

    summary: str

    keywords: list[str]