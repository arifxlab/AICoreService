"""
Tool schema definitions.
"""

from pydantic import BaseModel, Field


class ToolParameter(BaseModel):
    """
    Describes one tool parameter.
    """

    type: str

    description: str


class ToolDefinition(BaseModel):
    """
    Describes an AI callable tool.
    """

    name: str

    description: str

    properties: dict[str, ToolParameter] = Field(
        default_factory=dict
    )

    required: list[str] = Field(
        default_factory=list
    )